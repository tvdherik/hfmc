# File............ Main Simulation Class
# Author.......... Toby J. van den Herik
# Date Updated.... August 4th.

# 3rd party imports
from copy import deepcopy
from math import pi
from matplotlib import pyplot as plt

# hfmc imports
from hfmc.facilities import *
from hfmc.drivers import *
from hfmc.pretty import *
from hfmc.gasmodels import *
from hfmc.fluid import *

# a small interface function for creating the simulation flass
def newSimulation(simulation_name, facility, mode, driver_condition, fill_conditions, chemical_models, prove_convergence = False, further_refinement_factors = [], parallelise_refinement_proof = True, exclude_reactions = []):

    # Build and return a class with these inputs.

    return Simulation(simulation_name, facility, mode, driver_condition, fill_conditions, chemical_models, prove_convergence, further_refinement_factors, parallelise_refinement_proof, exclude_reactions)

#
# the main simulation class...
#

class Simulation():

    #
    # The main simulation class to build and execute eilmer simulations and to interpret them.
    #

    #
    # init function for the simulation class
    #

    def __init__(self, simulation_name, facility, mode, driver_condition, fill_conditions, chemical_models, prove_convergence, further_refinement_factors, parallelise_refinement_proof, exclude_reactions) -> None:

        # initialisations
        self.name = simulation_name
        self.facility = facility
        self.mode = mode
        self.fill_conditions = fill_conditions
        self.driver_condition = driver_condition
        self.prove_convergence = prove_convergence
        self.further_refinement_factors = further_refinement_factors
        self.parallelise_refinement_proof = parallelise_refinement_proof
        self.chemical_models = chemical_models
        self.exclude_reactions = exclude_reactions

        # input checking
        # facility allowed?
        if self.facility not in hfmc_facilities_dictionary:

            # has the user provided their own?
            if type(self.facility) == type(dict):
                # if the user provided a dict keep that
                inform("A user-provided dictionary is being used as the facility definition.", "update")
            else:
                # stop as we dont have a facility dict that is valid
                inform("Facility not found. Try one of "+f"{[fac for fac in hfmc_facilities_dictionary]}", "error", True)
                self.facility = hfmc_facilities_dictionary

        else:
            # else, we know the user gave a valid facility name, we'll use it...
            # turn self.facility from holding the name string to holding the actual facility dict
            self.facility = deepcopy(hfmc_facilities_dictionary[self.facility])
            # we have no deepcopied the facility dict from the default and it will remain uncorrupted.

        # mode within facility dict?
        if self.mode not in self.facility["modes"]:
            inform("Given facility mode is not set up in the given facility dictionary.", "error", True)
        else:
            # we'll do the same as for the facility and make
            # self.mode become the dict rather than the name of the mode.
            self.mode = self.facility["modes"][self.mode]["assembly"]

        # has the user defined the correct initial fill conditions for this mode?
        for key in self.mode:
            # get the fill state identity and ensure than the pressyre, temp, and composition is provided for each fill state (excl the driver if not cold gas).
            if self.mode[key]["style"] in ["driven-tube"]:
                state_id = self.mode[key]["initial-identity"]
                
                for prefix in ["T_", "p_", "molef_"]:

                    if (prefix+str(state_id)) not in self.fill_conditions:
                        inform("Missing initial fill condition: " + f"{prefix}{state_id} of State {state_id} not defined", "error", True)


        # has the user provided a valid driver dictionary or valid dictionary name?
        if type(self.driver_condition) == type(dict):
            #assume the user has supplied their own...
            inform("A user-provided dictionary is being used as the driver definition.", "update")
        elif self.driver_condition in hfmc_drivers_dictionary:
            #make the self.driver_condition be the dictionary rather than the name of the driver
            self.driver_condition = deepcopy(hfmc_drivers_dictionary[self.driver_condition])
        else:
            inform("The driver condition given must be a valid name or a dictionary definition", "error", True)

        return None

    #
    # Initialisation Fucntion for the Simulation
    #

    def initialise(self) -> None:

        #
        # Inform prepartions occuring...
        #

        inform(f"Initialising simulation, {self.name}", "update")


        # 
        # Prepare the gas model and chemistry files with the gdtk
        # 

        #get the species in the driver gas...
        for item_name in self.driver_condition:
            if "molef" in item_name:
                species_driver = [sp_name for sp_name in self.driver_condition[item_name]]
                break

        # get the species in all gas slugs...
        species_driven_slugs = []

        for item_name in self.mode:
            #if the part of the tunnel is a driven part, get the species in its initial fill condition
            if self.mode[item_name]["style"] == "driven-tube":
                #note the state_id
                #state_id = self.mode[item_name]["initial-identity"]

                #add each element to the driven list of species
                for element_name in self.fill_conditions:
                    if "molef" in element_name:
                        species_driven_slugs = [sp_name for sp_name in self.fill_conditions[element_name]]

        # a union set of all the species in all fill conditions...
        species_all = {sp for sp in species_driven_slugs}.union({sp for sp in species_driver})

        # what're the reaction scheme/s?

        if (len(self.chemical_models) == 0) :
            self.chemical_models = "thermally-perfect"
            inform("No chemical model defined. Assuming all gases are thermally perfect. Non-reacting.")

        # build the gas model and chemistry...
        possible_flow_species = buildChemicalScheme(self.chemical_models)

        # union the possible flow species from reaction schemes with those given by the above
        self.chemicals = sorted(species_all.union(possible_flow_species))
        buildGasModel(self.chemicals)
        
        #
        # Process the geometry... (make substitutions and ensure no perfect steps)
        #

        # determien the lenght of the driver and substitute any custom geometry
        self.substituteOrificeGeometry()
        self.substituteDriverLength()

        # this must be run after all geometry substitution is completed, replaces steps with a subtle slope.
        self.removePerfectSteps()

        #
        # Create a function that gives the initial state ID as a function of location
        #

        FuncStateGivenPosition = self.determineStateGivenPosition()
        FuncFillNameExpressionGivenID = self.determineFillNameExpressionGivenID()

        #
        # get all the gasblocks in order.
        #

        # add the location of the diaphragms to the geometry
        diaphragm_positions = [self.mode[element_name]["location"] for element_name in self.mode if "location" in self.mode[element_name]]

        # create a map of slugs fill IDs to their extents spatially
        ordered_identities = [self.mode[element_name]["initial-identity"] for element_name in self.mode if "initial-identity" in self.mode[element_name]]
        ordered_slug_extents = [self.facility["geometry"][0][0]] + diaphragm_positions + [self.facility["geometry"][-1][0]]

        # put diaphragm positions into geom and make new easier to reference self.geometry
        diaphragm_coords_list = [(pos, None, "diaphragm") for pos in diaphragm_positions]

        #merge the lists are sort by position, x.
        self.geometry = sorted(self.facility["geometry"] + diaphragm_coords_list, key=lambda x: x[0])
        
        #i'll store for later the blocks either side of a BC that is a diaphragm...
        self.BC_sets_with_diaphragm = []

        #assuming diaphragm cannot/willnot be put at the edge of the domain
        for (i, coord) in enumerate(self.geometry[0:-1]):
            if coord[1] == None:

                coord_L = self.geometry[i-1]
                coord_R = self.geometry[i+1]
                diam_at_diaphragm = (coord_L[1] + coord_R[1])/2

                if abs(coord[0] - coord_L[0]) < 1/self.facility["eilmer-configuration"]["cpm"]:
                    self.geometry[i-1] = (coord_L[0], coord_L[1], coord[2])
                else:                
                    self.geometry[i] = (coord[0], diam_at_diaphragm, coord[2])

        #pop any coords that were left as None as they were deemed too close to another point to be set as a diaphragm coord
        [self.geometry.pop(i) for (i,e) in enumerate(self.geometry) if e[1] == None]
        [self.BC_sets_with_diaphragm.append((i-1,i)) for (i,e) in enumerate(self.geometry[0:-1]) if "diaphragm" in e]

        #make the gas blocks
        self.gasblocks = {}
        block_id_counter = 0
        for (i, identity) in enumerate(ordered_identities):
            
            slug_bounds = [ordered_slug_extents[i], ordered_slug_extents[i+1]]
            fill_id = identity

            for (i, coord_L) in enumerate(self.geometry[0:-1]):

                coord_R = self.geometry[i+1]
                centre_of_block = (coord_L[0] + coord_R[0])/2

                boundary_conditions = "" #TODO

                #is the gasblock inside the current slug range of interest...
                if (centre_of_block > slug_bounds[0]) and (centre_of_block < slug_bounds[1]):
                    block_id_counter += 1
                    self.gasblocks[block_id_counter] = GasBlock(block_id_counter, coord_L, coord_R, self.facility["eilmer-configuration"]["cpm"], f"state_{fill_id}", boundary_conditions)
                    
                    
                    NB: get the diaphragm BC working properly to make sure that's not part of the issue.
                    then turn chem on!


        # 
        # Write the Eilmer simulation
        #

        with open("sim.lua", 'w') as sim_file:

            #setPreliminaryEilmerConfirguation(sim_file)
            writeln(sim_file, "\n--- ! HFMC Autogenerated Eilmer Simulation ! ---")
            writeln(sim_file, "\n--- Config...")
            writeln(sim_file, "nsp, nmodes, gm = setGasModel(\"gas.lua\")")
            
            # gas model fill states
            writeln(sim_file, "\n--- Initial Gas Model States...")
            for state in set(self.slugInitialIDsMap):
                writeln(sim_file, FuncFillNameExpressionGivenID(state))
            
            #gas block geometry etc
            writeln(sim_file, "\n--- Geometry Config, Fluid Block Creation, Boundary Conditions...")
            for block_id in self.gasblocks:
                writeln(sim_file, self.gasblocks[block_id].get_eilmer_expression())

            #setFinalEilmerConfiguation(sim_file)
            writeln(sim_file, "identifyBlockConnections()")

            pass

        return
    


















    #
    # Geometry Functionality
    #

    def substituteDriverLength(self):

        #if the driver is a cold gas driver take the driver lenght from the driver file (L_driver).
        if self.driver_condition["type"] in ["cold gas"]:

            for (i, coord) in enumerate(self.facility["geometry"]):

                #put the cold driven lenght in
                if coord[0] == "x_driver_start":
                    self.facility["geometry"][i] = (self.facility["geometry"][1][0] - L_driver, coord[1])

        #else... calculate the volume of the driver given the piston compression (this method does not consider overdrive)... (moving walls/piston dynamics are a TODO)
        elif self.driver_condition["type"] in ["free piston"]:

            if "gamma_4_polytropic" in self.driver_condition:
                gamma = self.driver_condition["gamma_4_polytropic"]
            else:
                pass #TODO need to create a gas model and get gamma from it 
            
            p_rupt = self.driver_condition["p_4"]
            p_init = self.driver_condition["p_4i"]
            T_init = self.driver_condition["T_4i"]
            v_init = self.driver_condition["V_4i"]

            v_final = v_init / ((p_rupt / p_init) ** (1/gamma))

            for (i, coord) in enumerate(self.facility["geometry"]):

                if coord[0] == "x_driver_start":

                    #put the compressed lenght in at rupture
                    L_driver = v_final / (pi * (coord[1]/2)**2)
                    self.facility["geometry"][i] = (self.facility["geometry"][1][0] - L_driver, coord[1])

            if self.driver_condition["T_4"] in ["solve-polytropic", "solve-isentropic"]:
                #solve either polytropic of isentropic (gamma will be set above based on if either is requested by the user)
                self.driver_condition["T_4"] = T_init * (p_rupt/p_init)**(1-(1/gamma))

        return None
    
    #a function to replace orifice geom given definition by driver condition
    def substituteOrificeGeometry(self):

        for (i, coord) in enumerate(self.facility["geometry"]):

            #if the coordinate is a string in teh y postion (D), find the variable with that name and sub it in
            if type(coord[1]) == str:

                if coord[1] in self.driver_condition:
                    
                    self.facility["geometry"][i] = (coord[0], self.driver_condition[coord[1]])

            #same for x pos (if ever needed)
            if type(coord[0]) == str:

                if coord[0] in self.driver_condition:
                    
                    self.facility["geometry"][i] = (self.driver_condition[coord[0]], coord[1])

        return None
    
    #
    # Ensure no prefect step geometry
    #
    
    def removePerfectSteps(self):

        cpm = self.facility["eilmer-configuration"]["cpm"]
        alternator = -1

        for (i, coord0) in enumerate(self.facility["geometry"]):

            #get the coord after it
            if i < (len(self.facility["geometry"])-1):
                coord1 = self.facility["geometry"][i+1]

            #are these two coords located in teh same x-position (are they a perfect step)
            if coord0[0] == coord1[0]:
                #perturb the current coord the "minimum unit" of 1 cpm (this may not be a good idea, this method needs to be validated)
                
                #ensure we alternate the director of geometry perturbation each time, else strange overlaps can occur for small geomtries (also a remind here to always check sim convergence!)
                alternator *= -1

                if alternator == -1:
                    self.facility["geometry"][i] = (self.facility["geometry"][i][0]+alternator*1/cpm, self.facility["geometry"][i][1])
                else:
                    self.facility["geometry"][i+1] = (self.facility["geometry"][i+1][0]+alternator*1/cpm, self.facility["geometry"][i+1][1])

        return None
    
    #
    # Make a function that returns state ID as a function of x
    #

    def determineStateGivenPosition(self):

        # # determine the start and end of slugs
        self.slugExtents = []

        #the left extent
        self.slugExtents.append(self.facility["geometry"][0][0]) #the left extent of all the gometry

        #the diaphragms
        for element_name in self.mode:
            element = self.mode[element_name]

            if element["style"] in ["diaphragm"]:
                self.slugExtents.append(element["location"])

        #the right extent
        self.slugExtents.append(self.facility["geometry"][-1][0]) #the right extent of all the gometry

        #determien ID between these locations...
        #self.slugInitialIDsMap = [self.mode[element_name]["initial-identity"] for element_name in self.mode if (self.mode[element_name]["style"] in ["driven-tube", "free-piston"])]

        self.slugInitialIDsMap = []
        for x in self.slugExtents:
            for (i,element_name) in enumerate(self.mode):
                element = self.mode[element_name]

                #set everying after a diaphragm (to the right) to the initial condition of the slug to the right
                if i < (len(self.mode)-1):
                    if element["style"] in ["diaphragm"]:
                        if x > element["location"]:
                            next_element = self.mode[list(self.mode.keys())[i+1]]
                            self.slugInitialIDsMap.append(next_element["initial-identity"])
                        elif x < 0: #and therefore not also beyond the first diaphragm, assume driver gas
                            self.slugInitialIDsMap.append("4")

        #print(self.slugInitialIDsMap)

        #this method relies on an ordered construction of gasslugs from left to right (which this code does)
        def Function(x):

            for (i, pos0) in enumerate(self.slugExtents):

                if i < (len(self.slugExtents)-1):

                    pos1 = self.slugExtents[i+1]

                    if (x > pos0) and (x < pos1):
                        return self.slugInitialIDsMap[i]

        return Function
    
    
    
    #
    # add all the chemicals to a fractions list and set them to zero
    #
    
    def getWholisticMoleFExpressionFromMoleF(self, fractions):

        for chem in self.chemicals:

            if chem not in fractions:

                fractions[chem] = 0.0
        
        return fractions
    

    def determineFillNameExpressionGivenID(self):

        def Function(ID):

            if ID not in ["4"]:
                for element_name in self.mode:
                        
                    if "initial-identity" in self.mode[element_name]:

                        if ID in (self.mode[element_name]["initial-identity"]):

                            p = self.fill_conditions[f"p_{ID}"]
                            T = self.fill_conditions[f"T_{ID}"]
                            molef = self.getWholisticMoleFExpressionFromMoleF(self.fill_conditions[f"molef_{ID}"]).__str__().replace(":", " =").replace("\'", "")

                            gm_gdtk_expression = [
                                f"massf_{ID} = gm:molef2massf({molef})",
                                f"state_{ID} = FlowState:new" + "{" + f"p = {p}, T = {T}, massf = massf_{ID}" + "}",

                            ]

                            eilmer_expression_final = ""
                            for line in gm_gdtk_expression:
                                eilmer_expression_final += line + "\n"

                            return eilmer_expression_final

                
            #handle the driver fill/compressed state differently (as it comes from the driver dict not the user-given fill condition dict)
            else:
                
                p = self.driver_condition[f"p_{ID}"]
                T = self.driver_condition[f"T_{ID}"]

                try:
                    molef = self.getWholisticMoleFExpressionFromMoleF(self.driver_condition[f"molef_{ID}i"]).__str__().replace(":", " =").replace("\'", "")
                except:
                    molef = self.getWholisticMoleFExpressionFromMoleF(self.driver_condition[f"molef_{ID}"]).__str__().replace(":", " =").replace("\'", "")

                gm_gdtk_expression = [
                    f"massf_{ID} = gm:molef2massf({molef})",
                    f"state_{ID} = FlowState:new" + "{" + f"p = {p}, T = {T}, massf = massf_{ID}" + "}",

                ] 

                eilmer_expression_final = ""
                for line in gm_gdtk_expression:
                    eilmer_expression_final += line + "\n"

                return eilmer_expression_final

        return Function

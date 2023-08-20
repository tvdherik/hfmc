# File............ Main Simulation Class
# Author.......... Toby J. van den Herik
# Date Updated.... August 4th.

# 3rd party imports
from copy import deepcopy

# hfmc imports
from hfmc.facilities import *
from hfmc.drivers import *
from hfmc.pretty import *
from hfmc.gasmodels import *

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


        self.substituteOrificeGeometry()
        self.substituteDriverLength()

        #this must be run after all geometry is substituted.
        self.removePerfectSteps()


        # 
        # Write the Eilmer simulation
        #


        with open("sim.lua", 'w') as sim_file:
        
            #setInitialEilmerConfig(sim_file)
            #setInitialStates(sim_file)

            #lose structure of block building...

            #for coordinate in geom...
            #   for (id, coord) enumerate(geometry list of coords)
            #       gasblock_expression = buildGasBlock(given coord1 and coord2, id)
            #        writeln(sim_file, gasblock expression)
            #
            #


            #setFinalEilmerConfiguation()

            pass

        return
    

    #
    # Geometry Functionality
    #

    def substituteDriverLength():

        return None
    
    def substituteOrificeGeometry():

        return None
    
    def removePerfectSteps():

        return None
# File............ Main Simulation Class
# Author.......... Toby J. van den Herik
# Date Updated.... August 4th.

# 3rd party imports
from copy import deepcopy

# hfmc imports
from hfmc.facilities import *
from hfmc.drivers import *
from hfmc.pretty import *

# a small interface function for creating the simulation flass
def newSimulation(simulation_name, facility, mode, fill_conditions, driver_condition, prove_convergence = False, further_refinement_factors = [], parallelise_refinement_proof = True):

    # Build and return a class with these inputs.

    return Simulation(simulation_name, facility, mode, fill_conditions, driver_condition, prove_convergence, further_refinement_factors, parallelise_refinement_proof)

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

    def __init__(self, simulation_name, facility, mode, fill_conditions, driver_condition, prove_convergence, further_refinement_factors, parallelise_refinement_proof) -> None:

        # initialisations
        self.name = simulation_name
        self.facility = facility
        self.mode = mode
        self.fill_conditions = fill_conditions
        self.driver_condition = driver_condition
        self.prove_convergence = prove_convergence
        self.further_refinement_factors = further_refinement_factors
        self.parallelise_refinement_proof = parallelise_refinement_proof

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


        return None

    #
    # Initialisation Fucntion for the Simulation
    #

    def initialise(self) -> None:



        return
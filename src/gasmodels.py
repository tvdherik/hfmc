# File............ Gas Model Construction and Relevant Functionality
# Author.......... Toby J. van den Herik
# Date Updated.... August 6th.
# Detail.......... When provided a set of species by the user, this functionality will make a reacting gas model with the gdtk and attempt to define relevant reactions.
#                  (the user can also specify further equations for reactions if they so wish)

#3rd party imports
import os

#hfmc imports
from hfmc.reactions import *
from hfmc.pretty import *

def buildGasModel(species_list) -> None:

    gas_file_input_name = 'gas.inp'
    gas_file_final_name = 'gas.lua'

    chem_file_input_name = "reactions.inp"
    chem_file_final_name = "chemistry.lua"

    # need to produce 2 manual files (a gas.inp file and reactions.inp) and use prep-gas and prep-chem to get processed gas models.
    with open(gas_file_input_name, 'w') as gasfile:

        writeln(gasfile, "-- \n" + "-- Automatically generated gas file by hfmc. \n"+"-- \n")
        writeln(gasfile, "model = \"thermally perfect gas\"")
        writeln(gasfile, "species = {" + str(species_list)[1:-1] +"}")

        gasfile.close()

    #compute the gas file from this input and chem (assumes chemistry input file was built first - needed to know all possible species)
    os.system(f"prep-gas {gas_file_input_name} {gas_file_final_name} > prep-gas-log.txt 2>&1")
    os.system(f"prep-chem {gas_file_final_name} {chem_file_input_name} {chem_file_final_name} > prep-chem-log.txt 2>&1")

    #build the chemistry/reacting schemes with gdtk format

    return None

def buildChemicalScheme(reaction_schemes):

    chem_file_input_name = "reactions.inp"
    chem_file_final_name = "chemistry.lua"
    possible_flow_species = set()

    with open(chem_file_input_name, 'w') as chem_file:

        writeln(chem_file, "-- \n" + "-- Automatically generated chemistry/reactions file by hfmc. \n"+"-- \n")
        
        try:
            for scheme in hfmc_reaction_configs_dictionary:
                
                if any(scheme in item for item in reaction_schemes):
                    writeln(chem_file, hfmc_reaction_configs_dictionary[scheme])

        except:
            inform("Chemical scheme is not implemented / known", "error", True)


        for reaction_name in hfmc_chemical_reactions_dictionary:

            reaction = hfmc_chemical_reactions_dictionary[reaction_name]

            if any(scheme in parent_sch for parent_sch in reaction.parent_schemes for scheme in reaction_schemes):
                
                #insert the reaction into the scheme file
                writeln(chem_file, reaction.gdtk_expression_block)

                #note all the inputs and products of the reaction
                chemicals = reaction.equation_string.split(" ") #get the chemicals
                chemicals = {X for X in chemicals if X not in ["<=>", "+", "M"]} #convert to a set excluding non-chemical elements of the equation (arrows, M arbitrary partner, etc)
                
                #union this set with the possible_flow_chemcials
                possible_flow_species = possible_flow_species.union(chemicals)                

    return sorted(possible_flow_species)

# small file writer wrapper function
def writeln(file, line):

    file.write(line+"\n")

    return None
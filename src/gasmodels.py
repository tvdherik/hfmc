# File............ Gas Model Construction and Relevant Functionality
# Author.......... Toby J. van den Herik
# Date Updated.... August 6th.
# Detail.......... When provided a set of species by the user, this functionality will make a reacting gas model with the gdtk and attempt to define relevant reactions.
#                  (the user can also specify further equations for reactions if they so wish)

#3rd party imports
import os

#hfmc imports
from hfmc.reactions import *

def buildGasModel(species_list, reaction_schemes) -> None:

    gas_file_input_name = 'gas.inp'
    gas_file_final_name = 'gas.lua'

    # need to produce 2 manual files (a gas.inp file and reactions.inp) and use prep-gas and prep-chem to get processed gas models.
    with open(gas_file_input_name, 'w') as gasfile:

        writeln(gasfile, "-- \n" + "-- Automatically generated gas file by hfmc. \n"+"-- \n")
        writeln(gasfile, "model = \"thermally perfect gas\"")
        writeln(gasfile, "species = {" + str(species_list)[1:-1] +"}")

        gasfile.close()

    #compute the gas file from this input
    os.system(f"prep-gas {gas_file_input_name} {gas_file_final_name} > prep-gas-log.txt 2>&1")

    #build the chemistry/reacting schemes with gdtk format

    


    return None

# small file writer wrapper function
def writeln(file, line):

    file.write(line+"\n")

    return None

#test
buildGasModel(["He", "O2", "O", "N2", "N", "N+", "e-"])
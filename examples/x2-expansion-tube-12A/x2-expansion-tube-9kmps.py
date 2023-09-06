
# File............ X2 Expansion Tube Example with hfmc.
# Author.......... Toby J. van den Herik
# Date Updated.... August 9th.

# 
# This is the python implementation 
# 

# import hfmc
from hfmc import *

#the initial/fill conditions...
fill_dictionary = {
    "T_1" : 300,
    "p_1" : 9000,
    "molef_1" : {"N2" : 0.78, "O2" : 0.22},
    "T_5" : 300,
    "p_5" : 18,
    "molef_5" : {"N2" : 0.78, "O2" : 0.22},
}

chem_model = ["Gupta1990-5sp"]

# create the simulation
sim = newSimulation("x2-sim-test-9kps", "x2", "expansion-tube", "x2-lwp-2.5mm-100He-0Ar-isentropic", fill_dictionary, chem_model)

# initialise the simulation
sim.initialise()

#print(sim.chemicals)

# execute the simulation
#sim.execute()

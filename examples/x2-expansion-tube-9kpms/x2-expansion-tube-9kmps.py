
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
    "p_1" : 3000,
    "molef_1" : {},
    "T_5" : 300,
    "p_5" : 3000,
    "molef_5" : {}
}

# create the simulation
sim = newSimulation("x2-sim-test", "x2", "expansion-tube", fill_dictionary, "x2-lwp-2.5mm")

# initialise the simulation
sim.initialise()

# execute the simulation
#sim.execute()

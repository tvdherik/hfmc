# File............ A class to handle all geometry / fluid block interface between hfmc formatting / input and eilmer4
# Author.......... Toby J. van den Herik
# Date Updated.... August 4th.


#Ex....

#
#                      o 
#                    / |
# o----------------o   |
# |                |   |    <---- an example of [2] blocks that might have the same initial fill or have a diaphragm in between.
# o----------------o---o 
#



class GasBlock():
    def __init__(self, x_left, x_right, geometry, initial_condition, boundary_conditions = []) -> None:

        for coordinate in geometry:
            
            #if coordinate is in the domain
            if (coordinate[0] >= x_left) and (coordinate[0] <= x_right):

        return None


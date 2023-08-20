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
    def __init__(self, identity, coord_left, coord_right, cpm, initial_condition, boundary_conditions = []) -> None:

        #fluid block identity
        self.identity = identity

        #fluid block extents (x1,d1), (x2,d2)
        self.x_left = coord_left[0]
        self.R_left = coord_left[1]/2 #<--diam to radius as sim is axyisymmetric
        self.x_right = coord_right[0]
        self.R_right = coord_right[1]/2 #<--diam to radius as sim is axyisymmetric

        #lenght of the fluid block
        self.lenght = abs(self.x_right - self.x_left)

        #cells per meter and total number of cells
        self.cpm = cpm
        self.num_cells = self.cpm * self.lenght

        #initial and boudnary condition handling
        self.initial_condition = initial_condition
        self.boundary_conditions = boundary_conditions

        return None
    
    def get_eilmer_expression(self):

        id = self.identity

        #block structure...

        #
        # p01-------------p11
        #  |               |
        # p00-------------p10
        # 

        #ill collapse this into per line before returning it...
        eilmer_expression = [

            f"-- block {id}",
            f"p00_{id} = Vector3:new"+"{"+f"x = {self.x_left}, y = {0.0}"+"}" +"; " + f"p01_{id} = Vector3:new"+"{"+f"x = {self.x_right}, y = {self.R_right}"+"}",
            f"p11_{id} = Vector3:new"+"{"+f"x = {self.x_left}, y = {self.R_left}"+"}" +"; " + f"p10_{id} = Vector3:new"+"{"+f"x = {self.x_right}, y = {0.0}"+"}",

            #do this with the grid maker that takes points not lines

            #f"patch_{id} = makePatch"+"{"+f"north = {}, south = {}, east = {}, west = {}"+"}",
            f"patch_{id} = CoonsPatch:new"+"{"+f"p00_{id}, p10_{id}, p11_{id}, p01_{id}"+"}",
            f"grid_{id}  = StructuredGrid:new"+"{"+f"psurface = patch_{id}, niv = {self.num_cells}, njv = 2"+"}",
            f"block_{id} = FluidBlock:new"+"{"+f"grid = grid_{id}, initialState = {self.initial_condition}"+"}",

        ]

        eilmer_expression_final = ""
        for line in eilmer_expression:
            eilmer_expression_final += line + "\n"

        return eilmer_expression_final
    
testBlock = GasBlock(1, (0,0.2), (1,0.2), 10, None, None)
string = testBlock.get_eilmer_expression()
print(string)
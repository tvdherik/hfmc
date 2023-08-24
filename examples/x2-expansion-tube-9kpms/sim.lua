-- block 0
p00_0 = Vector3:new{x = -0.21323728881206966, y = 0.0}; p01_0 = Vector3:new{x = -0.21323728881206966, y = 0.1284}
p11_0 = Vector3:new{x = -0.112, y = 0.1284}; p10_0 = Vector3:new{x = -0.112, y = 0.0}
patch_0 = CoonsPatch:new{p00 = p00_0, p10 = p10_0, p11 = p11_0, p01 = p01_0}
grid_0  = StructuredGrid:new{psurface = patch_0, niv = 17, njv = 2}
block_0 = FluidBlock:new{grid = grid_0, initialState = state_4}

-- block 1
p00_1 = Vector3:new{x = -0.112, y = 0.0}; p01_1 = Vector3:new{x = -0.112, y = 0.1284}
p11_1 = Vector3:new{x = -0.10533333333333333, y = 0.0425}; p10_1 = Vector3:new{x = -0.10533333333333333, y = 0.0}
patch_1 = CoonsPatch:new{p00 = p00_1, p10 = p10_1, p11 = p11_1, p01 = p01_1}
grid_1  = StructuredGrid:new{psurface = patch_1, niv = 3, njv = 2}
block_1 = FluidBlock:new{grid = grid_1, initialState = state_4}

-- block 2
p00_2 = Vector3:new{x = -0.10533333333333333, y = 0.0}; p01_2 = Vector3:new{x = -0.10533333333333333, y = 0.0425}
p11_2 = Vector3:new{x = -0.018666666666666665, y = 0.0425}; p10_2 = Vector3:new{x = -0.018666666666666665, y = 0.0}
patch_2 = CoonsPatch:new{p00 = p00_2, p10 = p10_2, p11 = p11_2, p01 = p01_2}
grid_2  = StructuredGrid:new{psurface = patch_2, niv = 15, njv = 2}
block_2 = FluidBlock:new{grid = grid_2, initialState = state_4}

-- block 3
p00_3 = Vector3:new{x = -0.018666666666666665, y = 0.0}; p01_3 = Vector3:new{x = -0.018666666666666665, y = 0.0425}
p11_3 = Vector3:new{x = -0.011999999999999997, y = 0.0325}; p10_3 = Vector3:new{x = -0.011999999999999997, y = 0.0}
patch_3 = CoonsPatch:new{p00 = p00_3, p10 = p10_3, p11 = p11_3, p01 = p01_3}
grid_3  = StructuredGrid:new{psurface = patch_3, niv = 3, njv = 2}
block_3 = FluidBlock:new{grid = grid_3, initialState = state_4}

-- block 4
p00_4 = Vector3:new{x = -0.011999999999999997, y = 0.0}; p01_4 = Vector3:new{x = -0.011999999999999997, y = 0.0325}
p11_4 = Vector3:new{x = 0.0, y = 0.0325}; p10_4 = Vector3:new{x = 0.0, y = 0.0}
patch_4 = CoonsPatch:new{p00 = p00_4, p10 = p10_4, p11 = p11_4, p01 = p01_4}
grid_4  = StructuredGrid:new{psurface = patch_4, niv = 3, njv = 2}
block_4 = FluidBlock:new{grid = grid_4, initialState = state_4}

-- block 5
p00_5 = Vector3:new{x = 0.0, y = 0.0}; p01_5 = Vector3:new{x = 0.0, y = 0.0325}
p11_5 = Vector3:new{x = 0.006666666666666667, y = 0.0425}; p10_5 = Vector3:new{x = 0.006666666666666667, y = 0.0}
patch_5 = CoonsPatch:new{p00 = p00_5, p10 = p10_5, p11 = p11_5, p01 = p01_5}
grid_5  = StructuredGrid:new{psurface = patch_5, niv = 3, njv = 2}
block_5 = FluidBlock:new{grid = grid_5, initialState = state_1}

-- block 6
p00_6 = Vector3:new{x = 0.006666666666666667, y = 0.0}; p01_6 = Vector3:new{x = 0.006666666666666667, y = 0.0425}
p11_6 = Vector3:new{x = 8.575, y = 0.0425}; p10_6 = Vector3:new{x = 8.575, y = 0.0}
patch_6 = CoonsPatch:new{p00 = p00_6, p10 = p10_6, p11 = p11_6, p01 = p01_6}
grid_6  = StructuredGrid:new{psurface = patch_6, niv = 1287, njv = 2}
block_6 = FluidBlock:new{grid = grid_6, initialState = state_5}

-- block 7
p00_7 = Vector3:new{x = 8.575, y = 0.0}; p01_7 = Vector3:new{x = 8.575, y = 0.0425}
p11_7 = Vector3:new{x = 8.598422, y = 0.04348}; p10_7 = Vector3:new{x = 8.598422, y = 0.0}
patch_7 = CoonsPatch:new{p00 = p00_7, p10 = p10_7, p11 = p11_7, p01 = p01_7}
grid_7  = StructuredGrid:new{psurface = patch_7, niv = 5, njv = 2}
block_7 = FluidBlock:new{grid = grid_7, initialState = state_5}

-- block 8
p00_8 = Vector3:new{x = 8.598422, y = 0.0}; p01_8 = Vector3:new{x = 8.598422, y = 0.04348}
p11_8 = Vector3:new{x = 8.627994, y = 0.044748}; p10_8 = Vector3:new{x = 8.627994, y = 0.0}
patch_8 = CoonsPatch:new{p00 = p00_8, p10 = p10_8, p11 = p11_8, p01 = p01_8}
grid_8  = StructuredGrid:new{psurface = patch_8, niv = 6, njv = 2}
block_8 = FluidBlock:new{grid = grid_8, initialState = state_5}

-- block 9
p00_9 = Vector3:new{x = 8.627994, y = 0.0}; p01_9 = Vector3:new{x = 8.627994, y = 0.044748}
p11_9 = Vector3:new{x = 8.664767, y = 0.046478}; p10_9 = Vector3:new{x = 8.664767, y = 0.0}
patch_9 = CoonsPatch:new{p00 = p00_9, p10 = p10_9, p11 = p11_9, p01 = p01_9}
grid_9  = StructuredGrid:new{psurface = patch_9, niv = 7, njv = 2}
block_9 = FluidBlock:new{grid = grid_9, initialState = state_5}

-- block 10
p00_10 = Vector3:new{x = 8.664767, y = 0.0}; p01_10 = Vector3:new{x = 8.664767, y = 0.046478}
p11_10 = Vector3:new{x = 8.709836, y = 0.048842}; p10_10 = Vector3:new{x = 8.709836, y = 0.0}
patch_10 = CoonsPatch:new{p00 = p00_10, p10 = p10_10, p11 = p11_10, p01 = p01_10}
grid_10  = StructuredGrid:new{psurface = patch_10, niv = 8, njv = 2}
block_10 = FluidBlock:new{grid = grid_10, initialState = state_5}

-- block 11
p00_11 = Vector3:new{x = 8.709836, y = 0.0}; p01_11 = Vector3:new{x = 8.709836, y = 0.048842}
p11_11 = Vector3:new{x = 8.764294999999999, y = 0.051939}; p10_11 = Vector3:new{x = 8.764294999999999, y = 0.0}
patch_11 = CoonsPatch:new{p00 = p00_11, p10 = p10_11, p11 = p11_11, p01 = p01_11}
grid_11  = StructuredGrid:new{psurface = patch_11, niv = 10, njv = 2}
block_11 = FluidBlock:new{grid = grid_11, initialState = state_5}

-- block 12
p00_12 = Vector3:new{x = 8.764294999999999, y = 0.0}; p01_12 = Vector3:new{x = 8.764294999999999, y = 0.051939}
p11_12 = Vector3:new{x = 8.829201999999999, y = 0.055822}; p10_12 = Vector3:new{x = 8.829201999999999, y = 0.0}
patch_12 = CoonsPatch:new{p00 = p00_12, p10 = p10_12, p11 = p11_12, p01 = p01_12}
grid_12  = StructuredGrid:new{psurface = patch_12, niv = 11, njv = 2}
block_12 = FluidBlock:new{grid = grid_12, initialState = state_5}

-- block 13
p00_13 = Vector3:new{x = 8.829201999999999, y = 0.0}; p01_13 = Vector3:new{x = 8.829201999999999, y = 0.055822}
p11_13 = Vector3:new{x = 8.905529, y = 0.060521}; p10_13 = Vector3:new{x = 8.905529, y = 0.0}
patch_13 = CoonsPatch:new{p00 = p00_13, p10 = p10_13, p11 = p11_13, p01 = p01_13}
grid_13  = StructuredGrid:new{psurface = patch_13, niv = 13, njv = 2}
block_13 = FluidBlock:new{grid = grid_13, initialState = state_5}

-- block 14
p00_14 = Vector3:new{x = 8.905529, y = 0.0}; p01_14 = Vector3:new{x = 8.905529, y = 0.060521}
p11_14 = Vector3:new{x = 8.994119, y = 0.066033}; p10_14 = Vector3:new{x = 8.994119, y = 0.0}
patch_14 = CoonsPatch:new{p00 = p00_14, p10 = p10_14, p11 = p11_14, p01 = p01_14}
grid_14  = StructuredGrid:new{psurface = patch_14, niv = 15, njv = 2}
block_14 = FluidBlock:new{grid = grid_14, initialState = state_5}

-- block 15
p00_15 = Vector3:new{x = 8.994119, y = 0.0}; p01_15 = Vector3:new{x = 8.994119, y = 0.066033}
p11_15 = Vector3:new{x = 9.095628, y = 0.072266}; p10_15 = Vector3:new{x = 9.095628, y = 0.0}
patch_15 = CoonsPatch:new{p00 = p00_15, p10 = p10_15, p11 = p11_15, p01 = p01_15}
grid_15  = StructuredGrid:new{psurface = patch_15, niv = 17, njv = 2}
block_15 = FluidBlock:new{grid = grid_15, initialState = state_5}

-- block 16
p00_16 = Vector3:new{x = 9.095628, y = 0.0}; p01_16 = Vector3:new{x = 9.095628, y = 0.072266}
p11_16 = Vector3:new{x = 9.210471, y = 0.078971}; p10_16 = Vector3:new{x = 9.210471, y = 0.0}
patch_16 = CoonsPatch:new{p00 = p00_16, p10 = p10_16, p11 = p11_16, p01 = p01_16}
grid_16  = StructuredGrid:new{psurface = patch_16, niv = 19, njv = 2}
block_16 = FluidBlock:new{grid = grid_16, initialState = state_5}

-- block 17
p00_17 = Vector3:new{x = 9.210471, y = 0.0}; p01_17 = Vector3:new{x = 9.210471, y = 0.078971}
p11_17 = Vector3:new{x = 9.338763, y = 0.085705}; p10_17 = Vector3:new{x = 9.338763, y = 0.0}
patch_17 = CoonsPatch:new{p00 = p00_17, p10 = p10_17, p11 = p11_17, p01 = p01_17}
grid_17  = StructuredGrid:new{psurface = patch_17, niv = 21, njv = 2}
block_17 = FluidBlock:new{grid = grid_17, initialState = state_5}

-- block 18
p00_18 = Vector3:new{x = 9.338763, y = 0.0}; p01_18 = Vector3:new{x = 9.338763, y = 0.085705}
p11_18 = Vector3:new{x = 9.480260999999999, y = 0.091856}; p10_18 = Vector3:new{x = 9.480260999999999, y = 0.0}
patch_18 = CoonsPatch:new{p00 = p00_18, p10 = p10_18, p11 = p11_18, p01 = p01_18}
grid_18  = StructuredGrid:new{psurface = patch_18, niv = 23, njv = 2}
block_18 = FluidBlock:new{grid = grid_18, initialState = state_5}

-- block 19
p00_19 = Vector3:new{x = 9.480260999999999, y = 0.0}; p01_19 = Vector3:new{x = 9.480260999999999, y = 0.091856}
p11_19 = Vector3:new{x = 9.634305999999999, y = 0.096749}; p10_19 = Vector3:new{x = 9.634305999999999, y = 0.0}
patch_19 = CoonsPatch:new{p00 = p00_19, p10 = p10_19, p11 = p11_19, p01 = p01_19}
grid_19  = StructuredGrid:new{psurface = patch_19, niv = 25, njv = 2}
block_19 = FluidBlock:new{grid = grid_19, initialState = state_5}

-- block 20
p00_20 = Vector3:new{x = 9.634305999999999, y = 0.0}; p01_20 = Vector3:new{x = 9.634305999999999, y = 0.096749}
p11_20 = Vector3:new{x = 9.82269, y = 0.099827}; p10_20 = Vector3:new{x = 9.82269, y = 0.0}
patch_20 = CoonsPatch:new{p00 = p00_20, p10 = p10_20, p11 = p11_20, p01 = p01_20}
grid_20  = StructuredGrid:new{psurface = patch_20, niv = 30, njv = 2}
block_20 = FluidBlock:new{grid = grid_20, initialState = state_5}

-- block 21
p00_21 = Vector3:new{x = 9.82269, y = 0.0}; p01_21 = Vector3:new{x = 9.82269, y = 0.099827}
p11_21 = Vector3:new{x = 9.968333333333334, y = 0.10084}; p10_21 = Vector3:new{x = 9.968333333333334, y = 0.0}
patch_21 = CoonsPatch:new{p00 = p00_21, p10 = p10_21, p11 = p11_21, p01 = p01_21}
grid_21  = StructuredGrid:new{psurface = patch_21, niv = 23, njv = 2}
block_21 = FluidBlock:new{grid = grid_21, initialState = state_5}

-- block 22
p00_22 = Vector3:new{x = 9.82269, y = 0.0}; p01_22 = Vector3:new{x = 9.82269, y = 0.099827}
p11_22 = Vector3:new{x = 9.968333333333334, y = 0.10084}; p10_22 = Vector3:new{x = 9.968333333333334, y = 0.0}
patch_22 = CoonsPatch:new{p00 = p00_22, p10 = p10_22, p11 = p11_22, p01 = p01_22}
grid_22  = StructuredGrid:new{psurface = patch_22, niv = 23, njv = 2}
block_22 = FluidBlock:new{grid = grid_22, initialState = state_5}


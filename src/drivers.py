"""
    "file-head" : "Facilities Available in hfmc",
    "author"    : "Toby J. van den Herik",
    "date"      : "July 28th",
"""

hfmc_drivers_dictionary = {

    #
    #       Drivers nominally for the X2 FACILITY..............
    # 

    "x2-lwp-2.5mm-100He-0Ar-isentropic" : {
        "type" : "free piston",
        "p_4i" : 77.2e3, #[Pa]
        "p_4" : 35.7e6, #[Pa]
        "T_4" : "solve-polytropic", #see documentation for options,
        "T_4i" : 300,
        "gamma_4_polytropic" : 1.61,
        "V_4i" : 0.2371, #[m^3] initial driver volume, pre-compression
        "molef_4i" : {"He" : 1.0, "Ar" : 0.0}, #molef
        "D_orifice" : 65/1000, #[m]
        "gm_4" : "thermally-perfect-he-ar-gas-model", #100% He by default,
    },
    
    "x2-lwp-1.2mm-80He-20Ar-isentropic" : {
        "type" : "free piston",
        "p_4i" : 110.3e3, #[Pa]
        "p_4" : 15.5e6, #[Pa]
        "T_4" : "solve-polytropic", #see documentation for options,
        "T_4i" : 300,
        "gamma_4_polytropic" : 1.62,
        "V_4i" : 0.2371, #[m^3] initial driver volume, pre-compression
        "molef_4i" : {"He" : 0.8, "Ar" : 0.2}, #molef
        "D_orifice" : 85/1000, #[m]
        "gm_4" : "thermally-perfect-he-ar-gas-model", #100% He by default,
    },

    "x2-cold-gas-6-MPa-100He-0Ar" : {
        "type" : "cold gas",
        "L_driver" : 0.3, #[m] length of cold gas driver.
        "p_4" : 6e6, #[Pa]
        "T_4" : 300, #[K] see documentation for options
        #"molef_He" : 100.0, #[mole fraction]
        #"molef_Ar" : 0.0, #[mole fraction]
        #"D_orifice" : 85/1000, #[m]
        #"gm_4" : "thermally-perfect-he-ar-gas-model" #100% He by default
    },
    
    #
    # Drivers for other facilities... TODO
    #
}

"""
    "file-head" : "Facilities Available in hfmc",
    "author"    : "Toby J. van den Herik",
    "date"      : "July 28th",
"""

hfmc_facilities_dictionary = {

    #
    # 
    #       X2 FACILITY..............
    # 
    # 

    "x2" : {

        "name"          : "X2",
        "facility-name" : "X2 Expansion Tube - Expansion Mode",
        "notes"         : "The X2 Expanion Tube in Expansion Mode, Single Driver (free-piston)",

        "geometry" : [
            ("x_driver_start", 0.2568),
            (-0.112, 0.2568), (-0.112, 0.085),
            (-0.011999999999999997, 0.085),
            (-0.011999999999999997, "D_orifice"),
            (0.0, "D_orifice"),
            (0, 0.085), (8.575, 0.085),
            (8.598422, 0.08696),
            (8.627994, 0.089496),
            (8.664767, 0.092956),
            (8.709836, 0.097684),
            (8.764294999999999, 0.103878),
            (8.829201999999999, 0.111644),
            (8.905529, 0.121042),
            (8.994119, 0.132066),
            (9.095628, 0.144532),
            (9.210471, 0.157942),
            (9.338763, 0.17141),
            (9.480260999999999, 0.183712),
            (9.634305999999999, 0.193498),
            (9.82269, 0.199654),
            (9.975, 0.20168)
        ],

        "modes" : {
            #the expansion tube mode
            "expansion-tube" : {
                
                "assembly" : {

                    "driver" : {
                        "style" : "free-piston",
                        "initial-identity" : "4",
                        "expanded-identity" : "3",
                    },

                    "primary-diaphragm" : {
                        "style" : "diaphragm",
                        "name" : "primary",
                        "location" : 0.0
                    },
                    
                    "shock-tube" : {
                        "style" : "driven-tube",
                        "initial-identity" : "1",
                        "processed-identity" : "2"
                    },

                    "secondary-diaphragm" : {
                        "style" : "diaphragm",
                        "name" : "secondary",
                        "location" : 2.0
                    },

                    "acceleration-tube" : {
                        "style" : "driven-tube",
                        "initial-identity" : "5",
                        "processed-identity" : "6"
                    }

                }
            },

            "secondary-driver" : {
                
                "assembly" : {

                    "driver" : {
                        "style" : "free-piston",
                        "initial-identity" : "4",
                        "expanded-identity" : "3",
                    },

                    "primary-diaphragm" : {
                        "style" : "diaphragm",
                        "name" : "primary",
                        "location" : 0.0
                    },

                    "secondary-driver" : {
                        "style" : "secondary-driver",
                        "name" : "secondary driver",
                        "initial-identity" : "sec1",
                        "processed-identity" : "sec2"

                    },

                    "secondary-diaphragm" : {
                        "style" : "diaphragm",
                        "name" : "secondary",
                        "location" : 2.0
                    },
                    
                    "shock-tube" : {
                        "style" : "driven-tube",
                        "initial-identity" : "1",
                        "processed-identity" : "2"
                    },

                    "tertiary-diaphragm" : {
                        "style" : "diaphragm",
                        "name" : "tertiary",
                        "location" : 3.0
                    },

                    "acceleration-tube" : {
                        "style" : "driven-tube",
                        "initial-identity" : "5",
                        "processed-identity" : "6"
                    }

                }
            },

            #NRST mode (non-reflected shock tube)
            "nrst" : {
                
                "assembly" : {

                    "driver" : {
                        "style" : "free-piston",
                        "initial-identity" : "4",
                        "expanded-identity" : "3",
                    },

                    "primary-diaphragm" : {
                        "style" : "diaphragm",
                        "name" : "primary",
                        "location" : 0.0
                    },
                    
                    "shock-tube" : {
                        "style" : "driven-tube",
                        "initial-identity" : "1",
                        "processed-identity" : "2"
                    },
                }
            },

            #the secondary driver mode...
        },

        "eilmer-configuration" : {
            "cpm" : 40, #cells per meter of spatial 
        }
    },

    #
    # 
    # 
    #       OTHER FACILITIES TO COME......
    # 
    # 
    #  

    #"x3"  : {},
    #"x3r" : {},
    #"t4"  : {},
    #"t5"  : {}, #todo.   :)
}
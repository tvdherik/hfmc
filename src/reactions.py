# File............ Finite Rate Reaction Databse and Class
# Author.......... Toby J. van den Herik
# Date Updated.... August 8th.

#a brief class to enable the simplified handling of reactions
class Reaction():
    def __init__(self, equation_string, gdtk_expression_block, author_string, parent_schemes) -> None:

        self.equation_string = equation_string
        self.gdtk_expression_block = gdtk_expression_block
        self.author_string = author_string
        self.parent_schemes = parent_schemes # which schemes does this reaction occur in

        return None
    
### Configurations for chemical reaction files
hfmc_reaction_configs_dictionary = {

    # Generic Gupta
    "Gupta1990" : """
Config{
    --Gupta validity range is up to 30,000 Kelvin
    tempLimits = {lower=300.0, upper=30000.0},
    tightTempCoupling = true,
    odeStep = {method='rkf', errTol=1.0e-5}
}
    """,

    #more to do
}

hfmc_chemical_reactions_dictionary = {

    #
    # First, the Gupta1990 reactions...
    #

    "O2 + M <=> O + O + M" : Reaction(
        
        equation_string = "O2 + M <=> O + O + M",
        gdtk_expression_block =
        """
Reaction{
    'O2 + M <=> O + O + M',
    fr={'Arrhenius', A=3.610e+18, n=-1.00, C=59400.00},
    br={'Arrhenius', A=3.010e+15, n=-0.50, C=0.0},
    label='r1',
    efficiencies={O2=9.0, N2=2.0, O=25.0, N=1.0, NO=1.0, ['NO+']=0.0, ['O2+']=0.0, ['N2+']=0.0, ['O+']=0.0, ['N+']=0.0, ['e-']=0.0}
}
        """,
        author_string =  "Gupta et. al. 1990",
        parent_schemes = ["Gupta1990-5sp", "Gupta1990-7sp", "Gupta1990-11sp"]
    ),    

    "N2 + M <=> N + N + M" : Reaction(

        equation_string = "N2 + M <=> N + N + M",
        gdtk_expression_block = 
        """
Reaction{
    'N2 + M <=> N + N + M',
    fr={'Arrhenius', A=1.920e+17, n=-0.50, C=113100.00},
    br={'Arrhenius', A=1.090e+16, n=-0.50, C=0.0},
    label='r2',
    efficiencies={O2=1.0, N2=2.5, O=1.0, N=0.0, NO=1.0, ['NO+']=0.0, ['O2+']=0.0, ['N2+']=0.0, ['O+']=0.0, ['N+']=0.0, ['e-']=0.0}
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-5sp", "Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "" : Reaction(

        equation_string = "N2 + N <=> N + N + N",
        gdtk_expression_block =
        """
Reaction{
   'N2 + N <=> N + N + N',
   fr={'Arrhenius', A=4.150e+22, n=-1.50, C=113100.00},
   br={'Arrhenius', A=2.320e+21, n=-1.50, C=0.0},
   label='r3'
}        
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-5sp", "Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "NO + M <=> N + O + M" : Reaction(

        equation_string = "NO + M <=> N + O + M",
        gdtk_expression_block =
        """
Reaction{
   'NO + M <=> N + O + M',
   fr={'Arrhenius', A=3.970e+20, n=-1.50, C=75600.00},
   br={'Arrhenius', A=1.010e+20, n=-1.50, C=0.0},
   label='r4',
   efficiencies={O2=1.0, N2=1.0, O=20.0, N=20.0, NO=20.0, ['NO+']=0.0, ['O2+']=0.0, ['N2+']=0.0, ['O+']=0.0, ['N+']=0.0, ['e-']=0.0}
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-5sp", "Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "NO + M <=> N + O + M" : Reaction(

        equation_string = "NO + M <=> N + O + M",
        gdtk_expression_block =
        """
Reaction{
   'NO + M <=> N + O + M',
   fr={'Arrhenius', A=3.970e+20, n=-1.50, C=75600.00},
   br={'Arrhenius', A=1.010e+20, n=-1.50, C=0.0},
   label='r4',
   efficiencies={O2=1.0, N2=1.0, O=20.0, N=20.0, NO=20.0, ['NO+']=0.0, ['O2+']=0.0, ['N2+']=0.0, ['O+']=0.0, ['N+']=0.0, ['e-']=0.0}
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-5sp", "Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "NO + O <=> O2 + N" : Reaction(

        equation_string = "NO + O <=> O2 + N",
        gdtk_expression_block =
        """
Reaction{
   'NO + O <=> O2 + N',
   fr={'Arrhenius', A=3.180e+09, n=1.00, C=19700.00},
   br={'Arrhenius', A=9.630e+11, n=0.50, C=3600.0},
   label='r5'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-5sp", "Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "N2 + O <=> NO + N" : Reaction(

        equation_string = "N2 + O <=> NO + N",
        gdtk_expression_block =
        """
Reaction{
   'N2 + O <=> NO + N',
   fr={'Arrhenius', A=6.750e+13, n=0.00, C=37500.00},
   br={'Arrhenius', A=1.500e+13, n=0.00, C=0.0},
   label='r6'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-5sp", "Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "N + O <=> NO+ + e-" : Reaction(

        equation_string = "N + O <=> NO+ + e-",
        gdtk_expression_block =
        """
Reaction{
   'N + O <=> NO+ + e-',
   fr={'Arrhenius', A=9.030e+09, n=0.50, C=32400.00},
   br={'Arrhenius', A=1.800e+19, n=-1.00, C=0.0},
   label='r7'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "O + e- <=> O+ + e- + e-" : Reaction(

        equation_string = "O + e- <=> O+ + e- + e-",
        gdtk_expression_block = 
        """
Reaction{
   'O + e- <=> O+ + e- + e-',
   fr={'Arrhenius', A=3.600e+31, n=-2.91, C=158000.00},
   br={'Arrhenius', A=2.200e+40, n=-4.50, C=0.0},
   label='r8'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),
    
    "N + e- <=> N+ + e- + e-" : Reaction(

        equation_string = "N + e- <=> N+ + e- + e-",
        gdtk_expression_block =
        """
Reaction{
   'N + e- <=> N+ + e- + e-',
   fr={'Arrhenius', A=1.100e+32, n=-3.14, C=169000.00},
   br={'Arrhenius', A=2.200e+40, n=-4.50, C=0.0},
   label='r9'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "O + O <=> O2+ + e-" : Reaction(

        equation_string = "O + O <=> O2+ + e-",
        gdtk_expression_block =
        """
Reaction{
   'O + O <=> O2+ + e-',
   fr={'Arrhenius', A=1.600e+17, n=-0.98, C=80800.00},
   br={'Arrhenius', A=8.020e+21, n=-1.50, C=0.0},
   label='r10'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "O + O2+ <=> O2 + O+" : Reaction(

        equation_string = "O + O2+ <=> O2 + O+",
        gdtk_expression_block =
        """
Reaction{
   'O + O2+ <=> O2 + O+',
   fr={'Arrhenius', A=2.920e+18, n=-1.11, C=28000.00},
   br={'Arrhenius', A=7.800e+11, n=0.50, C=0.0},
   label='r11'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "N2 + N+ <=> N + N2+" : Reaction(

        equation_string = "N2 + N+ <=> N + N2+",
        gdtk_expression_block = 
        """
Reaction{
   'N2 + N+ <=> N + N2+',
   fr={'Arrhenius', A=2.020e+11, n=0.81, C=13000.00},
   br={'Arrhenius', A=7.800e+11, n=0.50, C=0.0},
   label='r12'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "N + N <=> N2+ + e-" : Reaction(

        equation_string = "N + N <=> N2+ + e-",
        gdtk_expression_block =
        """
Reaction{
   'N + N <=> N2+ + e-',
   fr={'Arrhenius', A=1.400e+13, n=0.00, C=67800.00},
   br={'Arrhenius', A=1.500e+22, n=-1.50, C=0.0},
   label='r13'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "O2 + N2 <=> NO + NO+ + e-" : Reaction(

        equation_string = "O2 + N2 <=> NO + NO+ + e-",
        gdtk_expression_block = 
        """
Reaction{
   'O2 + N2 <=> NO + NO+ + e-',
   fr={'Arrhenius', A=1.380e+20, n=-1.84, C=141000.00},
   br={'Arrhenius', A=1.000e+24, n=-2.50, C=0.0},
   label='r14'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "NO + M <=> NO+ + e- + M" : Reaction(

        equation_string = "NO + M <=> NO+ + e- + M",
        gdtk_expression_block =
        """
Reaction{
   'NO + M <=> NO+ + e- + M',
   fr={'Arrhenius', A=2.200e+15, n=-0.35, C=100800.00},
   br={'Arrhenius', A=2.200e+26, n=-2.50, C=0.0},
   label='r15',
   efficiencies={O2=4.0, N2=1.0, O=0.0, N=0.0, NO=0.0, ['NO+']=0.0, ['O2+']=0.0, ['N2+']=0.0, ['O+']=0.0, ['N+']=0.0, ['e-']=0.0}
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-7sp", "Gupta1990-11sp"]
    ),

    "O + NO+ <=> NO + O+" : Reaction(

        equation_string = "O + NO+ <=> NO + O+",
        gdtk_expression_block =
        """
Reaction{
   'O + NO+ <=> NO + O+',
   fr={'Arrhenius', A=3.630e+15, n=-0.60, C=50800.00},
   br={'Arrhenius', A=1.500e+13, n=0.00, C=0.0},
   label='r16'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "N2 + O+ <=> O + N2+" : Reaction(

        equation_string = "N2 + O+ <=> O + N2+",
        gdtk_expression_block =
        """
Reaction{
   'N2 + O+ <=> O + N2+',
   fr={'Arrhenius', A=3.400e+19, n=-2.0, C=23000.00},
   br={'Arrhenius', A=2.480e+19, n=-2.20, C=0.0},
   label='r17'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "N + NO+ <=> NO + N+" : Reaction(

        equation_string = "N + NO+ <=> NO + N+",
        gdtk_expression_block = 
        """
Reaction{
   'N + NO+ <=> NO + N+',
   fr={'Arrhenius', A=1.000e+19, n=-0.93, C=61000.00},
   br={'Arrhenius', A=4.800e+14, n=0.00, C=0.0},
   label='r18'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "O2 + NO+ <=> NO + O2+" : Reaction(

        equation_string = "O2 + NO+ <=> NO + O2+",
        gdtk_expression_block = 
        """
Reaction{
   'O2 + NO+ <=> NO + O2+',
   fr={'Arrhenius', A=1.800e+15, n=0.17, C=33000.00},
   br={'Arrhenius', A=1.800e+13, n=0.50, C=0.0},
   label='r19'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

    "O + NO+ <=> O2 + N+" : Reaction(

        equation_string = "O + NO+ <=> O2 + N+",
        gdtk_expression_block = 
        """
Reaction{
   'O + NO+ <=> O2 + N+',
   fr={'Arrhenius', A=1.340e+13, n=0.31, C=77270.00},
   br={'Arrhenius', A=1.000e+14, n=0.00, C=0.0},
   label='r20'
}
        """,
        author_string =  "Gupta et. al. 1990",        
        parent_schemes = ["Gupta1990-11sp"]
    ),

}

## 
## File.... pretty.py
## Desc.... A file to contain a bunch of background functions to help with pretty printing / file making
## Auth.... Toby J. van den Herik
## Date.... June, 2023
##

# ----------------------------- #
#            imports            #
# ----------------------------- #

MODULE_NAME = " "

def inform(MSG, MODE, KILL = False):
    # inform the user of any happenings...
    
    # is the information an error?
    if MODE in ["ERROR", "error", "Error"]:
        #print(f"{MODULE_NAME}: Error! -- " + MSG + ".")
        print("Error! -- " + MSG + ".")
        
    # is the information an update for the user?
    if MODE in ["UPDATE", "update", "Update"]:
        #print(f"{MODULE_NAME}: " + MSG + ".")
        print(MSG + ".")

    if MODE not in ["ERROR", "error", "Error", "UPDATE", "update", "Update"]:
        print("Bad inform useage.")
        print(MODE)
        
    # should the program be terminated?
    if KILL == True:
        print(f"{MODULE_NAME}: Terminating program.")
        exit()
    
    return None

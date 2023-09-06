
        
            #setInitialEilmerConfig(sim_file)
            
            #use the FuncFillNameExpressionGivenID to specify the gas models and mass fractions
            for state in set(self.slugInitialIDsMap):
                writeln(sim_file, FuncFillNameExpressionGivenID(state))
            
            #loop to make gasblocks (including edges at diaphragm locations)
            self.geom_incl_diaphragms = self.facility["geometry"]

            #first i will add the diaphragm coordinate with a 3rd data point as a diaphragm flag
            #
            # wont add a gas block edge for the diaohragm if one is already there (within 1 mm)
            #
            #for element_name in self.mode:
            #    element = self.mode[element_name]

                #if element["style"] in ["diaphragm"]:

                 #   diaphragm_coord = (element["location"], None)

                  #  for (i, coord) in enumerate(self.geom_incl_diaphragms):

                   #     if (i < len(self.geom_incl_diaphragms)-1):

                    #        coord0 = coord
 #                           coord1 = self.geom_incl_diaphragms[i+1]
#
                            #if in between coords and last coord was no a diaphragm (in the same spot)
  #                          if (coord0[0] < diaphragm_coord[0]) and (diaphragm_coord[0] < coord1[0]) and (coord0[0] - coord1[0] < 1e-4):

   #                             y_diaphragm = coord0[1]
    #                            diaphragm_coord = (diaphragm_coord[0], y_diaphragm)
     #                           self.geom_incl_diaphragms = self.geom_incl_diaphragms[0:i] + [diaphragm_coord] + self.geom_incl_diaphragms[i:-1]






            #build the gas blocks with this geom with diaphragms located
            self.gasblocks = {}
            #for (block_identity, coord) in enumerate(self.geom_incl_diaphragms):

            #    if block_identity < (len(self.facility["geometry"])-1):
            #        coord0 = coord
            #        coord1 = self.facility["geometry"][block_identity+1]

                #determine fill condition identity
            #    x_centre_gas_block = (coord0[0] + coord1[0])/2
            #    fill_identity = FuncStateGivenPosition(x_centre_gas_block)

                #BC
            #    boundary_conditions = "" #FuncBoundaryConditionExpressionGivenID(fill_identity)

                #
            #    self.gasblocks[block_identity] = GasBlock(block_identity, coord0, coord1, self.facility["eilmer-configuration"]["cpm"], f"state_{fill_identity}", boundary_conditions)

            #    writeln(sim_file, self.gasblocks[block_identity].get_eilmer_expression())

            diaphragm_locations = []

            #get the diaphragm locations in a list.
            for element_name in self.mode:
                element = self.mode[element_name]

                if element["style"] in ["diaphragm"]:

                    diaphragm_coord = (element["location"], None)

                    diaphragm_locations.append(diaphragm_coord)

            #put the diaphragms into the geom coords and sort by height
            self.geom_incl_diaphragms = sorted(self.geom_incl_diaphragms + diaphragm_locations, key=lambda x: x[0])

            #assuming a diaphragm cannot be at an end, makes its diam the average of the diameters on either side. 
            #also assumes a two diaphragms wont be placed next to eachother, that there is a coord in between

            print(self.geom_incl_diaphragms)


            for (i, coord) in enumerate(self.geom_incl_diaphragms):
                
                if coord[1] == None:
                    self.geom_incl_diaphragms[i] = (self.geom_incl_diaphragms[i][0], (self.geom_incl_diaphragms[i+1][1] + self.geom_incl_diaphragms[i-1][1])/2)
                

            print(self.geom_incl_diaphragms)

            block_ticker = -1
            for state in set(self.slugInitialIDsMap):
                for (block_identity, coord0) in enumerate(self.geom_incl_diaphragms):
                    
                    #ensure not at last coord and everage block edges to block centre
                    if block_identity != (len(self.geom_incl_diaphragms)-1):

                        if block_identity > block_ticker:
                            block_ticker += 1

                            coord1 = self.geom_incl_diaphragms[block_identity+1]
                            block_state = FuncStateGivenPosition((coord0[0] + coord1[0])/2)

                            boundary_conditions = ""

                            self.gasblocks[block_identity] = GasBlock(block_identity, coord0, coord1, self.facility["eilmer-configuration"]["cpm"], f"state_{block_state}", boundary_conditions)

                            writeln(sim_file, self.gasblocks[block_identity].get_eilmer_expression())


            #    then put the above inside this.
            






















#
    # will return a function capable of building gasmodel expressions and flowstates for given fill condition IDs 
    #

    def determineFillNameExpressionGivenID(self):

        def Function(ID):

            if ID not in ["4"]:
                for element_name in self.mode:
                        
                    if "initial-identity" in self.mode[element_name]:

                        if ID in (self.mode[element_name]["initial-identity"]):

                            p = self.fill_conditions[f"p_{ID}"]
                            T = self.fill_conditions[f"T_{ID}"]
                            molef = self.getWholisticMassFracExpressionFromMoleF(self.fill_conditions[f"molef_{ID}"]).__str__().replace(":", " =").replace("\'", "")

                            gm_gdtk_expression = [
                                f"massf_{ID} = gm:molef2massf({molef})",
                                f"state_{ID} = FlowState:new" + "{" + f"p = {p}, T = {T}, massf = massf_{ID}" + "}",

                            ]

                            eilmer_expression_final = ""
                            for line in gm_gdtk_expression:
                                eilmer_expression_final += line + "\n"

                            return eilmer_expression_final

                
            #handle the driver fill/compressed state differently (as it comes from the driver dict not the user-given fill condition dict)
            else:
                
                p = self.driver_condition[f"p_{ID}"]
                T = self.driver_condition[f"T_{ID}"]

                try:
                    molef = self.getWholisticMassFracExpressionFromMoleF(self.driver_condition[f"molef_{ID}i"]).__str__().replace(":", " =").replace("\'", "")
                except:
                    molef = self.getWholisticMassFracExpressionFromMoleF(self.driver_condition[f"molef_{ID}"]).__str__().replace(":", " =").replace("\'", "")

                gm_gdtk_expression = [
                    f"massf_{ID} = gm:molef2massf({molef})",
                    f"state_{ID} = FlowState:new" + "{" + f"p = {p}, T = {T}, massf = massf_{ID}" + "}",

                ] 

                eilmer_expression_final = ""
                for line in gm_gdtk_expression:
                    eilmer_expression_final += line + "\n"

                return eilmer_expression_final

        return Function
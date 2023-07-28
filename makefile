##                          
## File.... makefile
## Desc.... Run with 'make install' in the terminal to install hfmc into default directory, hfmcisnt
## Auth.... Toby J. van den Herik
## Date.... July, 2023
##

INSTALL_DIR ?= $(HOME)/hfmcinst

install:
	@echo "Installing hfmc in directory $(INSTALL_DIR). Be sure this path is added to the PYTHONPATH (see the README)."

	- mkdir -p $(INSTALL_DIR)/lib
	cp *.py $(INSTALL_DIR)/lib

	- mkdir -p $(INSTALL_DIR)/share
	cp gases/*.lua $(INSTALL_DIR)/share

	@echo "\n ---- hfmc is now installed ----"

remove:
	rm -r $(INSTALL_DIR)
	@echo "$(INSTALL_DIR) cleaned. Ready for new 'make install' from /hfmc/src/."
	@echo "\n ---- hfmc removed ----"

reinstall:
	@echo "Removing and reinstalling hfmcinst."
	make remove
	make install
	@echo "\n ---- hfmc reinstalled ----"

#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys


### PANDA Imports ###
from direct.gui.DirectGui import DirectButton
from direct.gui.DirectGui import DirectEntry
from panda3d.core import TextNode

## Client Imports ##

########################################################################

class multiplayerGUI():
    def __init__(self, _mainmenu):
        # Ref
        self.mainmenu = _mainmenu

        # create a singlePlayer button
        self.menubtn0 = DirectButton(
            # Scale and position
            scale = 0.10,
            pos = (0,0,0.5),
            # Text
            text = "Host Game",
            # Frame
            # Functionality
            command = '')

       	# create a Lan button
        self.menubtn1 = DirectButton(
            # Scale and position
            scale = 0.10,
            pos = (0,0,0.3),
            # Text
            text = "Join Game",
            # Frame
            # Functionality
            command = '')

        # create a Exit button
        self.menubtn3 = DirectButton(
            # Scale and position
            scale = 0.10,
            pos = (0,0,-0.1),
            # Text
            text = "Back",
            # Frame
            # Functionality
            command = self.handleBack)

        self.hide()

    def show(self):
        self.menubtn0.show()
        self.menubtn1.show()
        self.menubtn3.show()

    def hide(self):
        self.menubtn0.hide()
        self.menubtn1.hide()
        self.menubtn3.hide()


    def handleHost(self):
        pass

    def handleJoin(self):
        # Move to Host / Join-Find games screen
        pass

    def handleOptions(self):
        pass

    def handleBack(self):
        self.hide()
        self.mainmenu.show()



# TESTING
#import direct.directbase.DirectStart
#gui = menuGUI()
#gui.show()
#base.run()
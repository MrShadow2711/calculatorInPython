from button import *
from display import *
from input import *
from numpad import *
from modemanager import *

class Calculator:
    def __init__(self):
        self.inputstring = ""
        self.modemanager = ModeManager(self)
        self.numpad = Numpad(self)
        Input.calculator = self

    def update(self):
        Display.update()

    #do NOT USE this method, use modemanager.setMode instead
    def setMode(self,button:Button):
        self.modemanager.setMode(button)

    #do NOT USE this method, use modemanager.setModeTo instead
    def setModeTo(self, mode:str):
        self.modemanager.setModeTo(mode)
    
    #do NOT USE this method, use modemanager.revertMode instead
    def revertMode(self):
        self.modemanager.revertMode

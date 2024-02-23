from mode import *
from mode_computation import *
from mode_differentiation import *
from mode_equation import *
from mode_table import *
from button import *
from display import *

class Calculator:
    def __init__(self):
        self.inputstring = ""
        self.buttons:list = self._createButtons()
        self.modes:dict = self._createModes()
        self.activeMode:Mode = self.modes["computation"]

    def buttonPressed(self,button:Button):
        if button.type == "modeselect":
            self.setMode(button)
        else:
            self.activeMode.input(button)
        
        Display.update()

    def setMode(self,button:Button):
        pass

    def setModeTo(self):
        pass

    def _createButtons(self):
        pass

    def _createModes(self):
        return {
            "computation": Mode_Computation(self),
            "differentiation": Mode_Differentiation(self),
            "equation": Mode_Equation(self),
            "table": Mode_Table(self),
        }

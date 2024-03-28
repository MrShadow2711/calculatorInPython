from mode import *
from mode_computation import *
from mode_differentiation import *
from mode_equation import *
from mode_table import *
from mode_modeselection import *
from mode_setup import *

class ModeManager:
    def __init__(self,calculator_reference):
        self.calculator = calculator_reference
        
        self.modes:dict = self._createModes()
        self.activeMode:Mode = self.modes["computation"]
        self.previousMode:Mode = self.modes["computation"]
    
    def setMode(self,button:Button):
        if button.value == "mode":
            self.setModeTo("modeselect")
            return
        
        if button.value == "setup":
            self.setModeTo("setup")
            return
        
        print("Fehler: Modus konnte nicht bestimmt werden")

    def setModeTo(self, mode:str):
        self.previousMode = self.activeMode
        self.activeMode = self.modes[mode]
    
    def revertMode(self):
        self.activeMode = self.previousMode

    def _createModes(self):
        return {
            "computation": Mode_Computation(self),
            "differentiation": Mode_Differentiation(self),
            "equation": Mode_Equation(self),
            "table": Mode_Table(self),
            "modeselect": Mode_ModeSelect(self),
            "setup": Mode_Setup(self)
        }
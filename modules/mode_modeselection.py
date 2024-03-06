from mode import *

class Mode_ModeSelect(Mode):
    def __init__(self, calculatorReference):
        self.calculator = calculatorReference
    
    def input(self, button:Button):
        if button.type != "number": return

        match button.value:
            case "1":
                self.calculator.setModeTo("computation")
            case "2":
                self.calculator.setModeTo("table")
            case "3":
                self.calculator.setModeTo("differentiation")
            case "4":
                self.calculator.setModeTo("equation")
            case _:
                pass
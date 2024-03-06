from mode import *
from setup import Setup

class Mode_Setup(Mode):
    def __init__(self, calculatorReference):
        self.calculator = calculatorReference

    def input(self,button):
        match button.value:
            case "1":
                Setup.setAngleToDegree()
            case "2":
                Setup.setAngleToRadian()
            case _:
                pass

        self.calculator.revertMode()
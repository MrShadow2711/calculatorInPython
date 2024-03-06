from mode import *

class Mode_Setup(Mode):
    def __init__(self, calculatorReference):
        self.calculator = calculatorReference

    def input(self,button):
        self.calculator.revertMode()
class Button:
    def __init__(self,calculatorReference,id,value="",type=""):
        self.calculator = calculatorReference
        self.type = type
        self.id = id
        self.value = value
    
    def onClick(self):
        self.calculator.buttonPressed(self)
        
class Button:
    def __init__(self,numbpadReference,id,value="",type=""):
        self.numbpad = numbpadReference
        self.type = type
        self.id = id
        self.value = value
    
    def onClick(self):
        self.numbpad.buttonPressed(self)
        
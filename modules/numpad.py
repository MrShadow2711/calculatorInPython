from button import Button

class Numpad:
    def __init__(self,calculator_reference):
        self.calculator = calculator_reference
        self.buttons:list = self._createButtons()

    def buttonPressed(self,button:Button):
        #print("button pressed")
        if button.type == "modsel":
            self.calculator.setMode(button)
        else:
            self.calculator.activeMode.input(button)
        
        self.calculator.update()

    def _createButtons(self):
        arr = []
        
        arr.append(Button(self,0,"0","number"))
        arr.append(Button(self,1,"1","number"))
        arr.append(Button(self,2,"2","number"))
        arr.append(Button(self,3,"3","number"))
        arr.append(Button(self,4,"4","number"))
        arr.append(Button(self,5,"5","number"))
        arr.append(Button(self,6,"6","number"))
        arr.append(Button(self,7,"7","number"))
        arr.append(Button(self,8,"8","number"))
        arr.append(Button(self,9,"9","number"))
        arr.append(Button(self,10,"π","number"))
        arr.append(Button(self,11,"e","number"))
        arr.append(Button(self,12,"a","variable"))
        arr.append(Button(self,13,"b","variable"))
        arr.append(Button(self,14,"c","variable"))
        arr.append(Button(self,15,"d","variable"))
        arr.append(Button(self,16,"x","variable"))
        arr.append(Button(self,17))
        arr.append(Button(self,18,"(","symbol"))
        arr.append(Button(self,19,")","symbol"))
        arr.append(Button(self,20,"^","operator"))
        arr.append(Button(self,21,"log","operator"))
        arr.append(Button(self,22,"sqrt","operator"))
        arr.append(Button(self,23,"root","operator"))
        arr.append(Button(self,24,"!","operator"))
        arr.append(Button(self,25,"sin","operator"))
        arr.append(Button(self,26,"arcsin","operator"))
        arr.append(Button(self,27,"cos","operator"))
        arr.append(Button(self,28,"arccos","operator"))
        arr.append(Button(self,29,"tan","operator"))
        arr.append(Button(self,30,"arctan","operator"))
        arr.append(Button(self,31))
        arr.append(Button(self,32))
        arr.append(Button(self,33))
        arr.append(Button(self,34))
        arr.append(Button(self,35))
        arr.append(Button(self,36,".","decimal"))
        arr.append(Button(self,37,"ans","answer"))
        arr.append(Button(self,38,"+","operator"))
        arr.append(Button(self,39,"-","operator"))
        arr.append(Button(self,40,"*","operator"))
        arr.append(Button(self,41,"/","operator"))
        arr.append(Button(self,42,"DEL","edit"))
        arr.append(Button(self,43,"CL","edit"))
        arr.append(Button(self,44,"undo","edit"))
        arr.append(Button(self,45,"redo","edit"))
        arr.append(Button(self,46,"up","navig"))
        arr.append(Button(self,47,"down","navig"))
        arr.append(Button(self,48,"left","navig"))
        arr.append(Button(self,49,"right","navig"))
        arr.append(Button(self,50,"mode","modsel"))
        arr.append(Button(self,51,"setup","modsel"))
        arr.append(Button(self,52))
        arr.append(Button(self,53))
        arr.append(Button(self,54))
        arr.append(Button(self,55))

        return arr

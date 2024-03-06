from mode import *

class Mode_Computation(Mode):
    def __init__(self, calculatorReference):
        super().__init__(calculatorReference)
    
    def input(self,button):
        if button.type == "equals":
            self.solve()
            return
        
        if button.type == "navig":
            match button.value:
                case "left":
                    Cursor.moveLeft()
                case "right":
                    Cursor.moveRight()
                case _:
                    print("Fehler, Cursormethode nicht gefunden")
            return
        
        if button.type == "edit":
            match button.value:
                case "DEL":
                    Input.delete()
                case "CL":
                    Input.clear()
                case "undo":
                    Input.undo()
                case _:
                    print("Fehler, Button nicht erkannt")
            return
        
        Input.add(button.value)

    
    def solve(self):
        operatorliste = ["+", "-", "*", "/"]
        Speicher = []
        i=0
        while i < len(self.calculator.inputstring):
            if self.calculator.inputstring[i] in operatorliste:
                x=i
                a = int(''.join(Speicher))
                print(a)
                Speicher=[]
                i+=1
            else:
                Speicher.append(self.calculator.inputstring[i])
                i+=1
        b = int(''.join(Speicher))
        if self.calculator.inputstring[x] == "+":
            print(a+b)
        elif self.calculator.inputstring[x] == "-":
            print(a-b)
        elif self.calculator.inputstring[x] == "*":
            print(a*b)
        elif self.calculator.inputstring[x] == "/":
            print(a/b)





        

        

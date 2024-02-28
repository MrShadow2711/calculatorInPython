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

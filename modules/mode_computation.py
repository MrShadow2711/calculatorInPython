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


    # def initial(self, long_operatorlist):
    #     long_operatorlist_initial = []
    #     for element in long_operatorlist:
    #         long_operatorlist_initial.append(element[0])
    #     return long_operatorlist_initial
        
    def slicer(self, long_operatorlist):
        long_operatorlist_slices = []
        for element in long_operatorlist:
            for part in element:
                long_operatorlist_slices.append(part)
        return long_operatorlist_slices


    def Convert(self, inputstring, operatorlist, long_operatorlist):
        # long_operatorlist_initial = self.initial(long_operatorlist)
        # print(long_operatorlist_initial)
        long_operatorlist_slices = self.slicer(long_operatorlist)
        Solve_list = []
        memory = []
        Test = True
        for element in inputstring:
            if element in operatorlist:
                Solve_list.append(''.join(memory))
                memory = []
                Solve_list.append(element)
            # elif element in long_operatorlist_initial:
            #     continue
            elif element in long_operatorlist_slices:
                if Test:
                    Solve_list.append(''.join(memory))
                    memory = []
                    Test=False
                else:
                    Test=False
                memory.append(element)
            else:
                try:
                    if memory[0] in long_operatorlist_slices:
                        Solve_list.append(''.join(memory))
                        memory = []
                        Test=True
                    else:
                        Test=True
                except:
                    Test=True
                memory.append(element)
        Solve_list.append(''.join(memory))
        while '' in Solve_list:
            Solve_list.remove('')
        return Solve_list



    def solve(self):
        operatorlist = ["+", "-", "*", "/", ")"]
        long_operatorlist = ["sin(", "arcsin(", "cos(", "arccos(", "tan(", "arctan("]
        Solve_list = self.Convert(self.calculator.inputstring, operatorlist, long_operatorlist)
        print(Solve_list)
        # Speicher = []
        # i=0
        # while i < len(self.calculator.inputstring):
        #     if self.calculator.inputstring[i] in operatorliste:
        #         x=i
        #         a = int(''.join(Speicher))
        #         Speicher=[]
        #         i+=1
        #     else:
        #         Speicher.append(self.calculator.inputstring[i])
        #         i+=1
        # b = int(''.join(Speicher))
        # if self.calculator.inputstring[x] == "+":
        #     print(a+b)
        # elif self.calculator.inputstring[x] == "-":
        #     print(a-b)
        # elif self.calculator.inputstring[x] == "*":
        #     print(a*b)
        # elif self.calculator.inputstring[x] == "/":
        #     print(a/b)





        

        

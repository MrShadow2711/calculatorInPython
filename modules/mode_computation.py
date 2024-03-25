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

        
    def letter_long_operatorlist(self, long_operatorlist, digit):
        long_operatorlist_letters = []
        for element in long_operatorlist:
            long_operatorlist_letters.append(element[digit-1])
        return long_operatorlist_letters


    def Convert(self, inputstring, operatorlist, long_operatorlist):
        #Liste wird erstellt
        Solve_list = []
        #Zahlenspeicher wird erstellt
        number_memory = []
        #i wird erstellt und auf 0 gesetzt
        i = 0
        #Ausschließen dieser Buchstaben als darauffolgende, da Vorkommen von "a" und "c" als programmierbare (einstellige) Variable, welche aber auch beim "arc...", "ans" und "cos" vorkommt
        second_letter = ("r", "n", "o")

        #Konvertieren der ersten Stellen (nur bis vorletzten Digit, da letztes noch abfragbar sein muss)
        while i <= len(inputstring)-2:
            #Einstellige Operatoren werden umgewandelt
            if inputstring[i] in operatorlist and inputstring[i+1] not in second_letter:
                #Zahlen-Speicher wird Liste hinzugefügt und geleert
                Solve_list.append(''.join(number_memory))
                number_memory = []
                #Einstelliger Operator wird Liste hinzugefügt
                Solve_list.append(inputstring[i])

            #Mehrstellige Operatoren werden umgewandelt
            elif inputstring[i] in self.letter_long_operatorlist(long_operatorlist, 1):
                #Zahlen-Speicher wird Liste hinzugefügt und geleert
                Solve_list.append(''.join(number_memory))
                number_memory = []
                #Speicher für Operator wird erstellt/geleert
                long_operator_memory = []
                #i wird so lange erhöht bis Ende des Operators erreicht ist
                while inputstring[i] != "(":
                    long_operator_memory.append(inputstring[i])
                    i += 1
                #Klammer wird dem Operator-Speicher hinzugefügt
                long_operator_memory.append("(")
                #Operator-Speicher wird der Liste hinzugefügt
                Solve_list.append(''.join(long_operator_memory))
            
            #Zahlen werden umgewandelt
            else:
                #Zahl wird dem Zahlen-Speicher hinzugefügt
                number_memory.append(inputstring[i])
            #Nächste Stelle wird untersucht
            i += 1

        #Letzte Stelle konvertieren
        #Einstelliger Operator wird umgewandelt
        if inputstring[-1] in operatorlist:
            #Zahlen-Speicher wird Liste hinzugefügt
            Solve_list.append(''.join(number_memory))
            #Einstelliger Operator wird Liste hinzugefügt
            Solve_list.append(inputstring[-1])
        else:
            #Zahl wird dem Zahlen-Speicher hinzugefügt
            number_memory.append(inputstring[-1])
            #Zahlen-Speicher wird Liste hinzugefügt
            Solve_list.append(''.join(number_memory))
        #Entfernen leerer Strings aus Liste
        while '' in Solve_list:
            Solve_list.remove('')
        #Zurückgeben der vollständigen Liste
        return Solve_list


    #The order of operations can be remembered by the acronym PEMDAS, which stands for:
    #parentheses, exponents, multiplication and division from left to right, and addition and subtraction from left to right.

    def parentheses(self, list):
        return list

    def exponents(self, list):
        return list

    def multiplication_and_division(self, list):
        return list

    def addition_and_subtraction(self, list):
        return list

    def solve(self):
        operatorlist = ["+", "-", "*", "/", "(", ")", "^", "π", "e", "a", "b", "c", "d", "!", ".", "="]
        long_operatorlist = ["sin(", "arcsin(", "cos(", "arccos(", "tan(", "arctan(", "log", "sqrt", "root", "ans"]
        Solve_list = self.Convert(self.calculator.inputstring, operatorlist, long_operatorlist)
        print(Solve_list)
        Solve_list=self.parentheses(Solve_list)
        Solve_list=self.exponents(Solve_list)
        Solve_list=self.multiplication_and_division(Solve_list)
        Solve_list=self.addition_and_subtraction(Solve_list)
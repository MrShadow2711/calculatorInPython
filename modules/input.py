class Input:
    calculator:object
    previousString = ""

    def add(value):
        Input._saveString()
        inputstring = Input.calculator.inputstring

        Input.calculator.inputstring = inputstring[:Cursor.position] + str(value) + inputstring[Cursor.position:]
        Cursor.moveRight(len(value))
    
    def delete():
        Input._saveString()
        inputstring = Input.calculator.inputstring

        Input.calculator.inputstring = inputstring[:Cursor.position] + inputstring[(Cursor.position + 1):]
        Cursor.moveLeft()
    
    def clear():
        Input._saveString()
        Input.calculator.inputstring = ""
        Cursor.position = 0
    
    def undo():
        Input.calculator.inputstring = Input.previousString
        Cursor.position = Cursor.previousPosition

    def _saveString():
        Input.previousString = Input.calculator.inputstring


class Cursor:
    position = 0
    previousPosition = 0

    def moveLeft(steps = 1):
        Cursor._savePosition()
        Cursor.position -= steps

        if Cursor.position < 0:
            Cursor.position = len(Input.calculator.inputstring) - 1
    
    def moveRight(steps = 1):
        Cursor._savePosition()
        Cursor.position += steps

        if Cursor.position > len(Input.calculator.inputstring):
            Cursor.position = 0

    def _savePosition():
        Cursor.previousPosition = Cursor.position
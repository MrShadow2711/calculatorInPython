from calculator import *

myCalculator = Calculator()

myCalculator.inputstring = "sin(12)+3*7-arccos(43)"
myCalculator.activeMode.solve()
myCalculator.inputstring = "745*arctan(12)/32+3*7-arccos(43)-tan(3)"
myCalculator.activeMode.solve()
myCalculator.inputstring = "25*3+27/34-17"
myCalculator.activeMode.solve()
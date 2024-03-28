from calculator import *
import test

myCalculator = Calculator()

test.modeselection(myCalculator)
print("---------------")
test.setup(myCalculator)
print("---------------")
print(test.table(myCalculator))

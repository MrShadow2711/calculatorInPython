from calculator import *
import random

def modeselection(calculator:Calculator):
    def test1():
        calculator.numpad.buttons[50].onClick()
        if not isinstance(calculator.activeMode, Mode_ModeSelect): return "failed"

        calculator.numpad.buttons[1].onClick()
        if not isinstance(calculator.activeMode, Mode_Computation): return "failed"
        
        calculator.numpad.buttons[50].onClick()
        calculator.numpad.buttons[2].onClick()
        if not isinstance(calculator.activeMode, Mode_Table): return "failed"
        
        calculator.numpad.buttons[50].onClick()
        calculator.numpad.buttons[3].onClick()
        if not isinstance(calculator.activeMode, Mode_Differentiation): return "failed"
        
        calculator.numpad.buttons[50].onClick()
        calculator.numpad.buttons[4].onClick()
        if not isinstance(calculator.activeMode, Mode_Equation): return "failed"

        return "passed"
    
    print("Test 1 " + test1())

def setup(calculator:Calculator):
    def testMethods():
        #Test 1
        Setup.setAngleToDegree()
        if Setup.angle != "degree": return "failed test 1"

        #Test 2
        Setup.setAngleToRadian()
        if Setup.angle != "radian": return "failed test 2"
        
        #Test 3
        Setup.setAngleToRadian()
        if Setup.angle != "radian": return "failed test 3"

        #Test 4
        Setup.setAngleToDegree()
        if Setup.angle != "degree": return "failed test 4"

        #Test 5
        Setup.setAngleToDegree()
        if Setup.angle != "degree": return "failed test 5"

        #Test 6
        Setup.setAngleToRadian()
        if Setup.angle != "radian": return "failed test 6"

        return "passed"

    def testButtons():
        #Test 1
        calculator.numpad.buttons[51].onClick()
        if not isinstance(calculator.activeMode, Mode_Setup): return "failed test 1"
        calculator.numpad.buttons[51].onClick()
        if calculator.activeMode != calculator.previousMode: return "failed test 1"

        #Test 2
        for i in range(100):
            rand = random.randint(1,2)

            calculator.numpad.buttons[51].onClick()
            calculator.numpad.buttons[rand].onClick()

            if calculator.activeMode != calculator.previousMode: return "failed test 2"
            if rand == 1 and Setup.angle != "degree": return "failed test 2"
            if rand == 2 and Setup.angle != "radian": return "failed test 2"
        
        return "passed"

    print("Test Methods: " + testMethods())
    print("Test Buttons: " + testButtons())

def table(calculator:Calculator):
    calculator.numpad.buttons[50].onClick()
    calculator.numpad.buttons[2].onClick()

    if not isinstance(calculator.activeMode, Mode_Table): return "test failed"
    return "passed"
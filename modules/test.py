from calculator import *

def modeselection(calculator:Calculator):
    def test1():
        calculator.buttons[50].onClick()
        if not isinstance(calculator.activeMode, Mode_ModeSelect): return "failed"

        calculator.buttons[1].onClick()
        if not isinstance(calculator.activeMode, Mode_Computation): return "failed"
        
        calculator.buttons[50].onClick()
        calculator.buttons[2].onClick()
        if not isinstance(calculator.activeMode, Mode_Table): return "failed"
        
        calculator.buttons[50].onClick()
        calculator.buttons[3].onClick()
        if not isinstance(calculator.activeMode, Mode_Differentiation): return "failed"
        
        calculator.buttons[50].onClick()
        calculator.buttons[4].onClick()
        if not isinstance(calculator.activeMode, Mode_Equation): return "failed"

        return "passed"
    
    print("Test 1 " + test1())
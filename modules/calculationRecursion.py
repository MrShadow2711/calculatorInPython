### im Array "tasks" unten im Dokument können weitere Aufgaben angehängt werden ###
import math

def solve(task:str) -> float:
    if task == "": return 0.0

    #hash operations
    index = 0
    while index < len(task):
        if task[index] == "#":
            hashCode = task[index:index + 3]

            openingBracketIndex = index + 3
            closingBracketIndex = getClosingBracketIndex(task,openingBracketIndex)

            bracketContent:str = task[openingBracketIndex + 1 : closingBracketIndex]
            solvedOperation = hashOperation(bracketContent, hashCode)

            task = task[:index] + str(solvedOperation) + task[closingBracketIndex + 1:]

        index += 1

    #bracket
    index = 0
    while index < len(task):
        if task[index] == ")": return "error"

        if task[index] == "(":
            closingBracketIndex = getClosingBracketIndex(task,index)
            bracketContent:str = task[index+1 : closingBracketIndex]
            task = task[:index] + str(solve(bracketContent)) + task[closingBracketIndex + 1:]
        
        index += 1

    #arithmetic operations
    #addidtion
    terms = task.split("+")
    if len(terms) > 1:
        return calculate(terms, "+")
    
    #substraction
    terms = task.split("-")
    if len(terms) > 1:
        return calculate(terms, "-")
    
    #multiplication
    terms = task.split("*")
    if len(terms) > 1:
        return calculate(terms, "*")
    
    #division
    terms = task.split("/")
    if len(terms) > 1:
        return calculate(terms, "/")

    return float(task)


def hashOperation(bracketContent, hashCode):
    match hashCode:
        case "#00":
            return math.sin(solve(bracketContent))
        case "#01":
            return math.asin(solve(bracketContent))
        case "#02":
            return math.cos(solve(bracketContent))
        case "#03":
            return math.acos(solve(bracketContent))
        case "#04":
            return math.tan(solve(bracketContent))
        case "#05":
            return math.atan(solve(bracketContent))
        case "#06":
            attributes = bracketContent.split(",")
            return math.pow(solve(attributes[0]),solve(attributes[1]))
        case "#07":
            return float(math.factorial(int(solve(bracketContent))))
        case _:
            print("operation hash code unnown")
            return "error"


def getClosingBracketIndex(task,openingBracketIndex):
    bracketDepth = 1
    for index in range(openingBracketIndex + 1, len(task)):
        if task[index] == "(":
            bracketDepth += 1
            continue

        if task[index] != ")": continue
        bracketDepth -= 1

        if bracketDepth > 0: continue
        return index
    

def calculate(terms:list[str], operator:str):
    solution = solve(terms[0])
    terms.pop(0)

    for term in terms:
        match operator:
            case "+":
                solution += solve(term)
            case "-":
                solution -= solve(term)
            case "*":
                solution *= solve(term)
            case "/":
                solution /= solve(term)
            case _:
                print("we got a problemo")
    
    return solution

if __name__ == "__main__":
    tasks = ["5*2-10+3*3-2/(1+3)*2", "2+4*(4*(2+3)+10)/5", "#06(2,3)", "#06(4*#07(3)+1,1/2)"]

    for task in tasks:
        print(task + " = " + str(solve(task)))

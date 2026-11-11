import functions

def getSymbol():
    symbol = input("Enter symbol (+,-,*,/, q - exit): ")
    return symbol

def getNumber():
    num = int(input("Enter number: "))
    return num

def doOperation(symbol):
    if symbol not in ['+', '-', '*', '/']:
        print("Error: Wrong operation")
        return

    try:
        num1 = getNumber()
        num2 = getNumber()

        match symbol:
            case '+':
                print(functions.sum(num1, num2))
            case '-':
                print(functions.rem(num1, num2))
            case '*':
                print(functions.mul(num1, num2))
            case '/':
                result = functions.div(num1, num2)
                if result != None:
                    print(result)

    except ValueError:
        print("Error: Enter only numbers")
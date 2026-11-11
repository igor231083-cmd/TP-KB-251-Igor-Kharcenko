import functions

class Operations:
    def getSymbol(self):
        symbol = input("Enter symbol (+,-,*,/, q - exit): ")
        return symbol

    def getNumber(self):
        num = int(input("Enter number: "))
        return num

    def doOperation(self, symbol):
        if symbol not in ['+', '-', '*', '/']:
            print("Error: Wrong operation")
            return

        try:
            num1 = self.getNumber()
            num2 = self.getNumber()

            calc = functions.Calculator(num1, num2)

            match symbol:
                case '+':
                    print(calc.sum())
                case '-':
                    print(calc.rem())
                case '*':
                    print(calc.mul())
                case '/':
                    result = calc.div()
                    if result != None:
                        print(result)

        except ValueError:
            print("Error: Enter only numbers")
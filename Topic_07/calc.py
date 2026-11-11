import operations

calc = operations.Operations()

while True:
    symbol = calc.getSymbol()

    if symbol == 'q':
        print("Exit")
        break

    calc.doOperation(symbol)
import functions
import operations

while True:
    symbol = operations.getSymbol()

    if symbol == 'q':
        print("Exit")
        break

    operations.doOperation(symbol)
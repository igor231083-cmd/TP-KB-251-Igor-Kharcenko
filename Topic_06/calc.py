import functions
import operations
import logging

logging.basicConfig(
    filename = "calculator.log",
    level = logging.INFO,
)

while True:
    symbol = operations.getSymbol()

    if symbol == 'q':
        print("Exit")
        logging.info("Exit")
        break

    operations.doOperation(symbol)
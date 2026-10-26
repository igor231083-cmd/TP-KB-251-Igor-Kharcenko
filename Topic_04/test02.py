def sum(num1, num2):
    result = num1 + num2
    return result

def rem(num1, num2):
    result = num1 - num2
    return result

def mul(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None


while True:
    try:
        symbol = input("Enter symbol (+,-,*,/, q - exit): ")

        if symbol == 'q':
            break

        if symbol not in ['+', '-', '*', '/']:
             print("Error: Wrong operation")
             continue
        
        num1 = int(input("Enter first num 1: "))
        num2 = int(input("Enter second num 2: "))

        match symbol:
            case '+':
                print(sum(num1, num2))
            case '-':
                print(rem(num1, num2))
            case '*':
                print(mul(num1, num2))
            case '/':
                result = div(num1, num2)
                if result != None:
                    print(result)

    except ValueError:
        print("Error: Enter only numbers")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
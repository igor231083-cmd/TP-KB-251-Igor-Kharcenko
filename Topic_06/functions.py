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
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
    if num2 != 0:
        result = num1 / num2
        return result
    else:
        print("less than 0")


num1 = int(input("Enter first num 1: "))
num2 = int(input("Enter second num 2: "))
symbol = input("Entet symbol (+,-,*,/): ")
if symbol == '+':
    print(sum(num1, num2))
elif symbol == '-':
    print(rem(num1, num2))
elif symbol == '*':
    print(mul(num1, num2))
elif symbol == '/':
    print(div(num1, num2))
else:
    print("Error, you are stupid if you cant write the correct symbol, so go away")

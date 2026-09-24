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
while True :
    num1 = int(input("Enter first num 1: "))
    num2 = int(input("Enter second num 2: "))
    symbol = input("Entet symbol (+,-,*,/): ")
    match symbol:
        case '+' : print(sum(num1, num2))
        case '-' : print(rem(num1, num2))
        case '*' : print(mul(num1, num2))
        case '/' : print(div(num1, num2))
        case 'q' : break
def discriminant(b,a,c):
    result = b*b - 4*a*c
    return result

def search(result):
    if result < 0:
        print("discriminant < 0")
    elif result > 0:
        print("discriminant > 0")
    else:
        print("discriminant = 0")

b = int(input("Enter b: "))
a = int(input("Enter a: "))
c = int(input("Enter c: "))
print(discriminant(b,a,c))
search(discriminant(b,a,c))
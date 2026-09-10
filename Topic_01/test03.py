def discriminant(b,a,c):
    result = b*b - 4*a*c
    return result

b = int(input("Enter b: "))
a = int(input("Enter a: "))
c = int(input("Enter c: "))
print(discriminant(b,a,c))
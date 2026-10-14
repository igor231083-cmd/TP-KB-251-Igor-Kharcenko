def FindingPosition(list, value):
    index = 0
    for name in list:
        if name < value:
            index += 1
        else:
            return index
    return index

list = [1, 5, 10, 15, 20]
print(list)
value = int(input("Write the number you want to insert: "))
print("Index: ",  FindingPosition(list, value))

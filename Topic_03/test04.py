def insert(list, value):
    list.append(value)
    list.sort()
    index = list.index(value)
    return index



list = [1, 5, 10, 15, 20]
print(list)
value = int(input("Write the number you want to insert: "))
print("Your number is listed by index: ",insert(list, value))
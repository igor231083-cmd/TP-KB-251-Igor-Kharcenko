globalList = [
    {"name":"Bob", "phone":"0631234567", "age":"20", "height":"180"},
    {"name":"Emma", "phone":"0631234567", "age":"19", "height":"165"},
    {"name":"Jon", "phone":"0631234567", "age":"21", "height":"175"},
    {"name":"Zak", "phone":"0631234567", "age":"22", "height":"185"}
]

def printAllList(listForPrinting):
    for item in listForPrinting:
        str = "Name = " + item["name"] + " Phone = " + item["phone"] + " Age = " + item["age"] + " Height = " + item["height"]
        print(str)

def findPosition(listForFinding, nameForFinding):
    index = 0
    for item in listForFinding:
        if item["name"] < nameForFinding:
            index += 1
        else:
            break
    return index

def addElemToSortedList(listForAdd, newElem):
    positionForInsert = findPosition(listForAdd, newElem["name"])
    listForAdd.insert(positionForInsert, newElem)
    return

def getElement():
    name = input("Please enter the name ")
    phone = input("Please enter the phone ")
    age = input("Please enter the age ")
    height = input("Please enter the height ")
    return {"name":name, "phone":phone, "age":age, "height":height}

def deleteElem(listForDel, name):
    indexForDel = findPosition(listForDel, name)
    if indexForDel < len(listForDel) and listForDel[indexForDel]["name"] == name:
        del listForDel[indexForDel]
        return True
    else:
        return False

def updeteElement(listForUpdate):
    nameForUpdate = input("Please enter the name for update ")
    indexForUpdate = findPosition(listForUpdate, nameForUpdate)

    if indexForUpdate < len(listForUpdate) and listForUpdate[indexForUpdate]["name"] == nameForUpdate:
        newName = input("Please enter the new name ")
        newPhone = input("Please enter the new phone ")
        newAge = input("Please enter the new age ")
        newHeight = input("Please enter the new height ")

        del listForUpdate[indexForUpdate]

        newElem = {"name":newName, "phone":newPhone, "age":newAge, "height":newHeight}
        addElemToSortedList(listForUpdate, newElem)
        return True
    else:
        return False


def main():
    while True:
        chouse = input("Please enter the command [C - add new elem, D - delete elem, P - print all List, U - update element, X - exit] ")
        match chouse:
            case "C" | "c":
                newElem = getElement()
                addElemToSortedList(globalList, newElem)
            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete ")
                if deleteElem(globalList, nameElemForDel):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")
            case "P" | "p":
                printAllList(globalList)
            case "U" | "u":
                if updeteElement(globalList):
                    print("Element has been updated")
                else:
                    print("Element hasn't been found")
            case "X" | "x":
                print("Exit")
                break
            case _:
                print("Wrong operation")


main()

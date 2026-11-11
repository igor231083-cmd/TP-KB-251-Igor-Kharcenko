import csv
from sys import argv


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


def loadFromCSV(fileName):
    students = []

    with open(fileName, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            newElem = {
                "name":row["Name"],
                "phone":row["Phone"],
                "age":row["Age"],
                "height":row["Height"]
            }
            addElemToSortedList(students, newElem)

    return students


def saveToCSV(fileName, listForSave):
    with open(fileName, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["Name", "Phone", "Age", "Height"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        for item in listForSave:
            writer.writerow({
                "Name":item["name"],
                "Phone":item["phone"],
                "Age":item["age"],
                "Height":item["height"]
            })


def main():
    if len(argv) < 2:
        print("Error: Enter CSV file name")
        print("Example: python lab_02.py lab2.csv")
        return

    fileName = argv[1]

    try:
        globalList = loadFromCSV(fileName)
    except FileNotFoundError:
        print("Error: File not found")
        return

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
                try:
                    saveToCSV(fileName, globalList)
                    print("List has been saved")
                    print("Exit")
                    break
                except OSError:
                    print("Error: Cannot save file")

            case _:
                print("Wrong operation")


if __name__ == "__main__":
    main()
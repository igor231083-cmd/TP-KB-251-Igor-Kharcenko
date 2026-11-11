from sys import argv
from Student import Student
from Utils import Utils

def main():
    if len(argv) < 2:
        print("Error: Enter CSV file name")
        return

    fileName = argv[1]
    utils = Utils()

    try:
        globalList = utils.loadFromCSV(fileName)
    except FileNotFoundError:
        print("Error: File not found")
        return

    while True:
        chouse = input("Please enter the command [C - add new elem, D - delete elem, P - print all List, U - update element, X - exit] ")

        match chouse:
            case "C" | "c":
                name = input("Please enter the name ")
                phone = input("Please enter the phone ")
                age = input("Please enter the age ")
                height = input("Please enter the height ")

                newElem = Student(name, phone, age, height)
                globalList.addElement(newElem)

            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete ")

                if globalList.deleteElement(nameElemForDel):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")

            case "P" | "p":
                globalList.printAllList()

            case "U" | "u":
                nameForUpdate = input("Please enter the name for update ")

                if globalList.findStudent(nameForUpdate) != None:
                    newName = input("Please enter the new name ")
                    newPhone = input("Please enter the new phone ")
                    newAge = input("Please enter the new age ")
                    newHeight = input("Please enter the new height ")

                    globalList.updateElement(nameForUpdate, newName, newPhone, newAge, newHeight)
                    print("Element has been updated")
                else:
                    print("Element hasn't been found")

            case "X" | "x":
                try:
                    utils.saveToCSV(fileName, globalList)
                    print("List has been saved")
                    print("Exit")
                    break
                except OSError:
                    print("Error: Cannot save file")

            case _:
                print("Wrong operation")


if __name__ == "__main__":
    main()
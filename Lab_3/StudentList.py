from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def printAllList(self):
        for item in self.students:
            print(item)

    def findPosition(self, name):
        index = 0
        for item in self.students:
            if item.name < name:
                index += 1
            else:
                break
        return index

    def addElement(self, newElem):
        positionForInsert = self.findPosition(newElem.name)
        self.students.insert(positionForInsert, newElem)
        return

    def findStudent(self, name):
        index = self.findPosition(name)

        if index < len(self.students) and self.students[index].name == name:
            return self.students[index]
        else:
            return None

    def deleteElement(self, name):
        indexForDel = self.findPosition(name)

        if indexForDel < len(self.students) and self.students[indexForDel].name == name:
            del self.students[indexForDel]
            return True
        else:
            return False

    def updateElement(self, name, newName, newPhone, newAge, newHeight):
        indexForUpdate = self.findPosition(name)

        if indexForUpdate < len(self.students) and self.students[indexForUpdate].name == name:
            del self.students[indexForUpdate]

            newElem = Student(newName, newPhone, newAge, newHeight)
            self.addElement(newElem)
            return True
        else:
            return False

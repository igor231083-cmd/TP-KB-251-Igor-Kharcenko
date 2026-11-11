import csv
from Student import Student
from StudentList import StudentList

class Utils:
    def loadFromCSV(self, fileName):
        students = StudentList()

        with open(fileName, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)

            for row in reader:
                newElem = Student(row[0], row[1], row[2], row[3])
                students.addElement(newElem)

        return students

    def saveToCSV(self, fileName, listForSave):
        with open(fileName, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Name", "Phone", "Age", "Height"])

            for item in listForSave.students:
                writer.writerow([item.name, item.phone, item.age, item.height])
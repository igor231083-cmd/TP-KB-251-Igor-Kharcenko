from Student import Student
from StudentList import StudentList
from Utils import Utils


def test_findPosition():
    students = StudentList()

    students.addElement(Student("Bob", "0631234567", "20", "180"))
    students.addElement(Student("Emma", "0631234567", "19", "165"))
    students.addElement(Student("Jon", "0631234567", "21", "175"))

    assert students.findPosition("Anna") == 0
    assert students.findPosition("Bob") == 0
    assert students.findPosition("Tom") == 3


def test_addElement():
    students = StudentList()

    students.addElement(Student("Zak", "0631234567", "22", "185"))
    students.addElement(Student("Bob", "0631234567", "20", "180"))
    students.addElement(Student("Emma", "0631234567", "19", "165"))

    assert students.students[0].name == "Bob"
    assert students.students[1].name == "Emma"
    assert students.students[2].name == "Zak"


def test_deleteElement():
    students = StudentList()

    students.addElement(Student("Bob", "0631234567", "20", "180"))
    students.addElement(Student("Emma", "0631234567", "19", "165"))

    assert students.deleteElement("Bob") == True
    assert students.students[0].name == "Emma"
    assert students.deleteElement("Alex") == False


def test_updateElement():
    students = StudentList()

    students.addElement(Student("Bob", "0631234567", "20", "180"))
    students.addElement(Student("Emma", "0631234567", "19", "165"))
    students.addElement(Student("Zak", "0631234567", "22", "185"))

    assert students.updateElement("Bob", "Tom", "0987654321", "25", "190") == True

    assert students.students[0].name == "Emma"
    assert students.students[1].name == "Tom"
    assert students.students[2].name == "Zak"

    assert students.students[1].phone == "0987654321"
    assert students.students[1].age == "25"
    assert students.students[1].height == "190"

    assert students.updateElement("Alex", "Max", "123", "20", "180") == False


def test_CSV(tmp_path):
    students = StudentList()

    students.addElement(Student("Bob", "0631234567", "20", "180"))
    students.addElement(Student("Emma", "0631234567", "19", "165"))

    fileName = str(tmp_path / "Book.csv")

    utils = Utils()
    utils.saveToCSV(fileName, students)

    listForLoad = utils.loadFromCSV(fileName)

    assert len(listForLoad.students) == 2
    assert listForLoad.students[0].name == "Bob"
    assert listForLoad.students[1].name == "Emma"
    assert listForLoad.students[0].age == "20"
    assert listForLoad.students[1].height == "165"


def test_printAllList(capsys):
    students = StudentList()

    students.addElement(Student("Bob", "0631234567", "20", "180"))
    students.printAllList()

    result = capsys.readouterr().out

    assert "Name = Bob" in result
    assert "Age = 20" in result

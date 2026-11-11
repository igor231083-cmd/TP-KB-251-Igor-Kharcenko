from lab02 import findPosition
from lab02 import addElemToSortedList
from lab02 import deleteElem
from lab02 import updeteElement
from lab02 import loadFromCSV
from lab02 import saveToCSV


def test_findPosition():
    listForFinding = [
        {"name":"Bob", "phone":"0631234567", "age":"20", "height":"180"},
        {"name":"Emma", "phone":"0631234567", "age":"19", "height":"165"},
        {"name":"Jon", "phone":"0631234567", "age":"21", "height":"175"},
        {"name":"Zak", "phone":"0631234567", "age":"22", "height":"185"}
    ]

    assert findPosition(listForFinding, "Anna") == 0
    assert findPosition(listForFinding, "Bob") == 0
    assert findPosition(listForFinding, "Tom") == 3
    assert findPosition(listForFinding, "Zak") == 3


def test_addElement():
    listForAdd = [
        {"name":"Bob", "phone":"0631234567", "age":"20", "height":"180"},
        {"name":"Emma", "phone":"0631234567", "age":"19", "height":"165"},
        {"name":"Jon", "phone":"0631234567", "age":"21", "height":"175"}
    ]

    addElemToSortedList(listForAdd, {"name":"Anna", "phone":"12121212", "age":"18", "height":"170"})
    assert listForAdd[0]["name"] == "Anna"

    addElemToSortedList(listForAdd, {"name":"Tom", "phone":"12121212", "age":"20", "height":"180"})
    assert listForAdd[4]["name"] == "Tom"

    addElemToSortedList(listForAdd, {"name":"Zak", "phone":"12121212", "age":"22", "height":"185"})
    assert listForAdd[5]["name"] == "Zak"


def test_deleteElement():
    listForDel = [
        {"name":"Bob", "phone":"0631234567", "age":"20", "height":"180"},
        {"name":"Emma", "phone":"0631234567", "age":"19", "height":"165"},
        {"name":"Jon", "phone":"0631234567", "age":"21", "height":"175"},
        {"name":"Zak", "phone":"0631234567", "age":"22", "height":"185"}
    ]

    assert listForDel[0]["name"] == "Bob"
    assert deleteElem(listForDel, "Bob") == True
    assert listForDel[0]["name"] == "Emma"

    assert deleteElem(listForDel, "Alex") == False


def test_updateElement(monkeypatch):
    listForUpdate = [
        {"name":"Bob", "phone":"0631234567", "age":"20", "height":"180"},
        {"name":"Emma", "phone":"0631234567", "age":"19", "height":"165"},
        {"name":"Jon", "phone":"0631234567", "age":"21", "height":"175"},
        {"name":"Zak", "phone":"0631234567", "age":"22", "height":"185"}
    ]

    answers = iter(["Bob", "Tom", "0987654321", "25", "190"])
    monkeypatch.setattr("builtins.input", lambda text: next(answers))

    assert updeteElement(listForUpdate) == True
    assert listForUpdate[2]["name"] == "Tom"
    assert listForUpdate[2]["phone"] == "0987654321"
    assert listForUpdate[2]["age"] == "25"
    assert listForUpdate[2]["height"] == "190"
    assert listForUpdate[3]["name"] == "Zak"


def test_CSV(tmp_path):
    listForSave = [
        {"name":"Bob", "phone":"0631234567", "age":"20", "height":"180"},
        {"name":"Emma", "phone":"0631234567", "age":"19", "height":"165"}
    ]

    fileName = str(tmp_path / "test.csv")

    saveToCSV(fileName, listForSave)
    listForLoad = loadFromCSV(fileName)

    assert len(listForLoad) == 2
    assert listForLoad[0]["name"] == "Bob"
    assert listForLoad[1]["name"] == "Emma"
    assert listForLoad[0]["age"] == "20"
    assert listForLoad[1]["height"] == "165"
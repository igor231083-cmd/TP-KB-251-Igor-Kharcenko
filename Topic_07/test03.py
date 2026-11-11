class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name = " + self.name + " Age = " + str(self.age)


students = [
    Student("Zak", 22),
    Student("Bob", 20),
    Student("Emma", 19),
    Student("Jon", 21)
]

sortedStudents = sorted(students, key=lambda item: item.name)

for student in sortedStudents:
    print(student)
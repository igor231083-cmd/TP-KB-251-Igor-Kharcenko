class Student:
    def __init__(self, name, phone, age, height):
        self.name = name
        self.phone = phone
        self.age = age
        self.height = height

    def __str__(self):
        return "Name = " + self.name + " Phone = " + self.phone + " Age = " + self.age + " Height = " + self.height
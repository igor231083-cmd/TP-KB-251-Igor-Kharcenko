class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name = " + self.name + " Age = " + str(self.age)


person1 = Person("Bob", 20)
person2 = Person("Emma", 19)

print(person1)
print(person2)
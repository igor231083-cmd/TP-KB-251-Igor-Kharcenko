students = [
    {"name": "Zak", "grade": 80},
    {"name": "Bob", "grade": 95},
    {"name": "Emma", "grade": 75},
    {"name": "Jon", "grade": 90}
]

sortedByName = sorted(students, key=lambda item: item["name"])
sortedByGrade = sorted(students, key=lambda item: item["grade"])

print("Sorted by name:")
for item in sortedByName:
    print(item)

print("Sorted by grade:")
for item in sortedByGrade:
    print(item)
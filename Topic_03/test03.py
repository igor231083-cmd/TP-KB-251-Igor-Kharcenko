dict = {"a": 1, "b": 2, "c": 3}
print("1. Just text",dict)

dict.update({"d": 4, "e": 5})
print("2. Update",dict)

del dict["b"]
print("3. Del",dict)

print("4. Keys",dict.keys())

print("5. Values",dict.values())

print("6. Items",dict.items())

dict.clear()
print("7. Clear",dict)
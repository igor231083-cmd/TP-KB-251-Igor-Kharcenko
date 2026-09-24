list = [10, 30, 20]
print("1. Just text",list)

extra_items = [50, 60]
list.extend(extra_items)
print("2. Extend",list)

list.append(40)
print("3. Append",list)

list.insert(1, 15)
print("4. Insert",list)

list.remove(30)
print("5. Remove",list)

copied_list = list.copy()
print("6. Copy_original",list)
print("6. Copy_original",copied_list)

list.sort()
print("7. Sort",list)

list.clear()
print("8. Clear_original",list)
print("8. Clear_copy",copied_list)
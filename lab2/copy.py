# We can not just write list1 = list2, because list2 will be a "shadow" of list1 and all changes in list1 will affect to list1
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
list1.append(128)
print(list2)
print(list1)
list3 = list(list1)
print(list3)
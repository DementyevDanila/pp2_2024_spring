list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list4 = list1.copy()
list6 = [4, 5, 6]
list3 = list1 + list2
print(list3)

for x in list2:
    list4.append(x)

print(list4)

list6.extend(list1)
print(list6)
fruits = ["apple", "banana", "cherry", "banana", "dragonfruit", "TOMATO???"]
fruits.remove("banana") # method removes only first banana
print(fruits)
fruits.pop(1) #removing by index
print(fruits)
fruits.pop() #removes last item
print(fruits)
del fruits[0] #also removes item by index
print(fruits)
fruits.clear() #removes all items
print(fruits)
del fruits #removes all list

fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # add neew element to the end of list
print(fruits) 

tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical) # conect (fruits) with (tropical) 
print(fruits)
# extend() method can conect different types of data
thistuple = ("kiwi", "coconut")
fruits.extend(thistuple)
print(fruits)

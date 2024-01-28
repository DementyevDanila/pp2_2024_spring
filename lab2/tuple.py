# Tuples are used to store multiple items in a single variable.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

fruits_but_tuple = ("apple", "banana", "cherry")
print(fruits_but_tuple)

more_fruits = ("apple", "banana", "cherry", "apple", "banana")
print(more_fruits)
print(len(more_fruits))

new_tuple = ("apple",) # to create tule with 1 element I must use , after it
print(type(new_tuple))

tuple5 = ("apple") # string
print(type(tuple5)) 

tuple1 = ("abc", 34, True, 40, "male") # tupple can consist any type of data

aboba = tuple(("apple", "banana", "cherry")) 
print(aboba)
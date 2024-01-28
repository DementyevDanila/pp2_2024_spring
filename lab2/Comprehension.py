fruits = ["apple", "banana", "kiwi", "LIME????", "cherry", "orange"]
cool_fruits = []
for x in fruits:
    if "a" in x:
      cool_fruits.append(x)  
print(cool_fruits)
other_fruits = [x for x in fruits if "e" in x]
print(other_fruits)

# newlist = [expression for item in iterable if condition == True] syntax 

# The condition is optional and can be omitted:
newlist = [x for x in fruits] 
print (newlist)

# The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['coco gjambo' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "mango" for x in fruits] #"Return the item if it is not banana, if it is banana return orange".
print(newlist)

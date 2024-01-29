# there is 2 ways to delete 1 defifnite item from set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # if banana is not exist in thisset, program output error
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") # when discard method returns unchanged set
print(thisset)

# if u wanna play Russian Roulete, u can use method pop() to delete random item

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# method clear() emptie the set, while del keyworg removes totally

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset

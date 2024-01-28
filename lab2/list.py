# List is a collection which is ordered and changeable. Allows duplicate members.
# List elements starts from [0]
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

mylist = ["paper", "rock", "scissors"]
print (mylist)

# It possible to have same elements in one list.
newlist = ["paper", "paper", "scissors", "rock", "rock", "scissors"]
print (newlist)
print (len(newlist)) # how many elements now in list
intlist = [1, 2, 3, 5, 8, 445786, 0]
strlist = ["apple", "cigarette", "book"]
boolist = [True, True, False]
# Moreover, list can contain a gifferent types of data type.
mixlist = list(("drill", False, 487446, True, -8.78)) # It possible to create list with comand list()

print(type(mixlist)) # Wow, class is list

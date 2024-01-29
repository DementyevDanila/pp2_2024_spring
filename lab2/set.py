# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Set items are unchangeable, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets cannot have two items with the same value.\
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2, 0, False} # The values True and 1,  and False and 0, are considered the same value in sets, and are treated as duplicates:
print(thisset)

thisset = {"apple", "banana", "cherry", 0, False, 8956}
print(len(thisset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
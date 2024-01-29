set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set4 = set1

set3 = set1.union(set2)
set4.update(set2) #methods works with duplicates

print(set3)
print(set4)
# Intersection

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) # The intersection_update() method will keep only the items that are present in both sets.

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) # The intersection() method will return a new set, that only contains the items that are present in both sets.

print(z)
# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

print(x)    

x = {"apple", "banana", "cherry", True, 0}
y = {"google", "microsoft", "apple", 1, False}

z = x.symmetric_difference(y) # The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

print(z)



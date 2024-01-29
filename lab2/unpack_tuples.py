fruits = ("apple", "banana", "cherry") # It calls "packing" tuple

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# It calls "unpacking" tuple. We extract the values back into variables.

#Using Asterick *

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #it means that we create variablea with names green, yellow ang list with name red. * symbol means that after banana all elements will be added to "red" list

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits #in this example to the "tropick" list will assign values to the variable until the number of values left matches the number of variables left.

print(green)
print(tropic)
print(red)
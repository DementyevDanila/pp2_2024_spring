fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print(" ")

for i in range(len(fruits)):
    print(fruits[i])

print(" ")

veg = ["potato", "carrot", 'tomato', "cucumber"]

i = 0
while i < len(veg) :
    print(veg[i])
    i += 1
print(" ")
[print(x) for x in veg]
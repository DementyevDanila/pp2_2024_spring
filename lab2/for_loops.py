fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(1, 6): #(1, 6) notation means that counting starts from 1 and goes to 6
  print(x)
for x in range(2, 30, 3): #(2, 30, 3) notation means that counting starts from 2 and increasing by step 3 to a 30
  print(x)
print(' ')
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print(' ')
#nested if, like 2d array
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
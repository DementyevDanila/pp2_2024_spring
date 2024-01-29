thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict: # Print all key names
  print(x)
print(' ')
# or
for x in thisdict.keys():
  print(x)
print(' ')
for x in thisdict: # Print all values 
  print(thisdict[x])
print(" ")
# or
for x in thisdict.values(): # Print all values 
  print(x)
print(" ")

for x, y in thisdict.items(): # Loop through both keys and values, by using the items() method
  print(x, y)

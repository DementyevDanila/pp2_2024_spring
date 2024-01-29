thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y = thisdict.get("model") # gives same result
print (x == y)

car = {
"brand": "Dementyev",
"model": "Danila",
"year": 2006
}

x = car.keys() # The keys() method will return a list of all the keys in the dictionary.
print(x) #before the change
car["color"] = "white"
print(x) #after the change



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values() # The values() method will return a list of all the values in the dictionary.
print(x) #before the change
car["year"] = 2020
car["color"] = "orange"
print(x) #after the change



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items() # The items() method will return each item in a dictionary, as tuples in a list.
print(x) #before the change
car["year"] = 2020
car["color"] = "orange"
print(x) #after the change



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
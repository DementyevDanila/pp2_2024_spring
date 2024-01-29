# Dictionary is a collection which is ordered and changeable. No duplicate members.
# It's like a map in c++

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} # can contain differnt types of data
print(thisdict)
print(thisdict["brand"]) # brand is key to Ford

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  # "year": 2020 dictionary cant contain 1 key with 2 items 
}
print(len(thisdict)) #how many keys contains dictionary

thisdict = dict(name = "John", age = 36, country = "Norway") # methos dict() also creates dictionary
print(thisdict)
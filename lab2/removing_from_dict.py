
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color" : "pink",
  "price" : "withdrawn from sale"
}
print(thisdict) 
thisdict.popitem() # The popitem() method removes the last inserted item
print(thisdict) 
del thisdict["color"]
print(thisdict) 
thisdict.pop("model")
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict
# like we did previously, we can change value of specific key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"price": "300$"}) # The update() method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key:value pairs.
print(thisdict)


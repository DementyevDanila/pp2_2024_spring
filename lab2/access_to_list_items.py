listik = ["red", "orange", "blue"]
print(listik[1])
print(listik[-1]) # print first element from the end of list (blue)
listik = ["red", "orange", "blue", "yellow", "purple", "green", "magenta"]
print(listik[2:5]) # create a new list which consist elements from second(blue) to the fifth(green), but fifth is not exists. Like [2;5)
print(listik[:4]) #print all element till fourth 
print(listik[2:]) #print all element from second to end
print(listik[-4:-1])
if "black" in listik:
    print("Black among us")
else:
    print("Black war rejected")
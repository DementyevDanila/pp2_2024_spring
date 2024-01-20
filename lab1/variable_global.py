x = "Python"

def blob():
    print ("I love " + x)
blob()

y = "Mom and Dad" 

def blub():
    y = "Friends"   #now var y is local in function blub, I can use meaning "Friends" only in this function
    print("I love my " + y)

blub()

print ("I love my " + y)

def blyb():
    global z
    z = "The Witcher"

blyb()

print (z + " is awesome game")
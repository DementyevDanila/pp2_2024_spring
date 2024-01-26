print (10 > 9)
print (10 < 9)
print (10 == 10)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

#Any string is True, except empty strings. Any number is True, except 0. Any list, tuple, set, and dictionary are True, except empty ones.

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
# all False



def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))
# isinstance() function, which can be used to determine if an object is of a certain data type
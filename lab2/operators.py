# Arithmetic operators
x = 5
y = 2
print (x // y) # #the floor division // rounds the result down to the nearest whole number
# answer is 2

print (y ** x) # y in power of x

print (x % y) #remainder from division, x / y


# Assignment Operators

x = 5

x += 3 # same with x = x + 3
x -= 3 # same with x = x - 3
x *= 3 # same with x = x * 3
x %= 3 # same with x = x % 3
x **= 3 # same with x = x ** 3
x <<= 3 #same with x = x << 3 / побитовый сдвиг влево на 3

x = 5

x &= 3

print(x)


# Comparison Operators

x = 5
y = 3
print (x == y) # returns False, because 5 /= 3
print (x != y) # returns True, because 5 /= 3
print (x > y) # returns True. because 5 > 3
# also, there exist <; <=; >=

# Logical Operators

x = 7 

print (x > 5 and x < 12) # return True, if both conditions are True
print (x > 5 or x > 128) #return True, if one or more will be True
print (not(x < 5 and x < 10)) # return reverse result of (x < 5 and x < 10)
print(" ")

# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x is not y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print (" ")

# Membership Operators

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

# Bitwise Operators

print (6 & 3) # output is 2, because & operator returns 1 if both elements are 1. In this example 6 is 110 and 3 is 011. By comparing each bit, & returns 010 which equal to 2.
print (6 | 3) # output is 7, because | operator returns 1 if one element is 1. 110 and 011, all 0 will exchange to 1s.
print (6 ^ 3) # output is 5, because ^ operator returns 1 if both elemets different. In out case, 110 and 011, second bits are the same, so our notation will change to 101.
print (~3) # output is -4, because ~ operator inverts al bits.
print (3 << 2) # output is 12, because << operator add 2 zeros on the right side. 011 -> 0110 -> 01100
print (3 >> 1) # output is 1, because operator >> add 1 zeros on the left side. 011 -> 001
# Precedence operator

# Operator precedence describes the order in which operations are performed.
print((6 + 3) - (6 + 3))

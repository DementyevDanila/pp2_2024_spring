x = 1 #int
y = 2.5 #float
z = 1j #complex

x = 1
y = 35656222554887711
z = -548643218

print(type(x), type(y), type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x), type(y), type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x), type(y), type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x), type(y), type(z))

#how to convert number from one type to another

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#You cannot convert complex numbers into another number type.


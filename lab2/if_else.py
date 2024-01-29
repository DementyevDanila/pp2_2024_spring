a = 2
b = 4
c = 4
if a > b: 
    print("HoHoHo")
elif a == b: # else if, if the previous conditions were not true, then try this condition
    print("HiHiHi")
else:
    print("HaHaHa")
if c == b: print("Nice")
print("A") if a > b else print("B")
print("C") if c > b else print("=") if b == c else print("B")
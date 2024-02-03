def is_polin(x):    
    y = ""
    for i in range(len(x) - 1, -1, -1):
        y += x[i]

    if x == y:
        print("Yes")
    else:
        print("No")

str = input()
is_polin(str)
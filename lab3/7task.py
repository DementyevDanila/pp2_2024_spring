def has_33(num):
    cnt = 0
    for x in num:
        if x == 3:
            cnt += 1
            if cnt == 2: 
                return True
                break
        else:
            cnt = 0
        
num = input()
num = num.split()
print(type(num))
newlist = list(map(int, num))
print(type(newlist))

if has_33(newlist):
    print("True")
else:
    print("False")

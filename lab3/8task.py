def spy_among_us(p):
    cnt = 0
    for x in p:
        if x == 0:
            cnt += 1
        if (x == 7 and cnt == 2): 
            return True
            break
        if x != 0:
            cnt = 0

num = input()
num = num.split()
newlist = list(map(int, num))

if spy_among_us(newlist):
    print("True")
else:
    print("False")

        

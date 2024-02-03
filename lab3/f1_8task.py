def spy_among_us(p):
    cnt = 0
    che = False
    for x in p:
        if x == 0:
            cnt += 1
        if (x == 7 and cnt == 2): 
            print("True")
            che = True
            break
        if x != 0:
            cnt = 0
    if (che == False):
        print("False")
num = input()
num = num.split()
newlist = list(map(int, num))

spy_among_us(newlist)
def has_33(num):
    cnt = 0
    chk = False
    for x in num:
        if x == 3:
            cnt += 1
            if cnt == 2: 
                print("True")
                chk = True
                break
        else:
            cnt = 0
    if (chk == False):
        print("False")

num = input()
num = num.split()
newlist = list(map(int, num))

has_33(newlist)
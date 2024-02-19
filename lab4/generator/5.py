def genik(start):
    num = start
    while num != 0:
        yield num 
        num -= 1

N = int(input())
for i in genik(N):
    print(i, end = " ")
def genik(stop):
    num = 0
    while num <= stop:
        yield num * num 
        num += 1

N = int(input())
for i in genik(N):
    print(i, end = " ")
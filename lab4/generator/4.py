def squares(start, stop):
    num = start
    while num <= stop:
        yield num * num 
        num += 1

S = int(input())
N = int(input())

for i in squares(S, N):
    print(i, end = " ")
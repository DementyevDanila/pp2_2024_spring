def even_gen(stop):
    num = 0
    while num <= stop:
        if num % 2 == 0:
            yield num
        num += 1

Boarder = int(input())

for i in even_gen(Boarder):
    print(i, end = ",")
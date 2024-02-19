def div_by_12(stopslovo):
    num = 0
    while num <= stopslovo:
        if num % 3 == 0 and num % 4 == 0:
            yield num
        num += 1
blob = int(input())

for i in div_by_12(blob):
    print(i, end = " ")
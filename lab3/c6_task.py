def filter(ls):
    sublist = []
    for x in ls:
        checker = 0
        i = 1
        while (i <= x):
            if x == 1:
                sublist.append(x)
            if x % i == 0 :
                checker += 1
            if checker > 2:
                break
            i += 1
        if checker == 2: sublist.append(x)
    print(sublist)

numbers = input()
numbers = numbers.split()
newlist = list(map(int, numbers))

filter(newlist)
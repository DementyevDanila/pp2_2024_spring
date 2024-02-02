def prime(x):
    checker = 0
    i = 1
    while (i <= x):
        if x == 1:
            return True
        if x % i == 0 :
            checker += 1
        if checker > 2:
            return False
        i += 1
    if checker == 2: return True


numbers = input()
numbers = numbers.split()
newlist = list(map(int, numbers))

primes = []
for x in newlist:
    if prime(x):
        primes.append(x)
print(primes)
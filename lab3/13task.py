import random

def guess_num(name, attempt):
    print("Okay " + name + ", I guessed the number from 1 to 20. Try to guess it!")
    x = random.randrange(1, 20)
    checker = True
    cnt = 0
    while(checker == True):
        attempt = int(input())
        if(attempt == x):
            print("Ho Ho Ho, you guessed my number in", cnt + 1, "attempts!")
            checker = False
        if(attempt < x):
            print(":( Try a bit higher")
            cnt += 1
        if(attempt > x):
            print(":( Try a bit lower")
            cnt += 1


    
print("Hello, what is yor name?")
z = input()
k = ""
guess_num(z, k)
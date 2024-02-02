chicken = 35
rabbit = 0
checker = True
while(checker == True):
    if ((chicken * 2) + (rabbit * 4) == 94) :
        checker = False
    else:
        chicken -= 1
        rabbit += 1
print("Number of chickens: ", chicken)
print("Number of rabbits: ", rabbit)

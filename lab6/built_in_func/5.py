t = (1, 1, True, True, 1)
t2 = (0, 1, True, False, 1)
def true_checker(tup):
    check = True
    for x in tup:
        if(x == True):
            continue
        else:
            check = False
            print("All elements are not True")
            break
    if (check):
        print("All elements are True")

true_checker(t)
true_checker(t2)

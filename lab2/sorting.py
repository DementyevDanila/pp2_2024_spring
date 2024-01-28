thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

num = [100, 50, 65, 82, 23]
num.sort()
print(num)

thislist.sort(reverse = True) #sorted and reversed list
print(thislist)

def filter (n) :
    return abs(n -50)

num.sort(key = filter)
print(num)

fruits = ["Orange", "cherry", "aPPLE", "Mango"] # capital letters have higher precedence than lower 
fruits.sort()
print(fruits)

fruits.sort(key = str.lower)
print(fruits)

fruits.reverse()
print(fruits)
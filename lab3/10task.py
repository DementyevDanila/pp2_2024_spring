def only_un(l):
    l.sort()
    state = ""
    i = 0
    while i < len(l):
        if l[i] != state:
            state = l[i]
        elif (l[i] == state):
            l.remove(l[i])
            i -= 1
        i += 1

newlist = input()
newlist = newlist.split()
only_un(newlist)
print(newlist)
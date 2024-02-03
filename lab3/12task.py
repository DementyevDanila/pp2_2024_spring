def histo(l):
    for i in range (len(l)):
        print("*" * l[i])

salam = input()
salam = salam.split()
newlistik = list(map(int, salam))
histo(newlistik)
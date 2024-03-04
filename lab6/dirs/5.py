import os

path = r"\\DANILA\Users\pokam\Desktop\My education\pp2\lab6\test_folder"

f = open("biba.txt", "wt")
newlist = ["salam", "interesno", "ono", "kak", "eto", "vivedet"]
str = ""
for i in range(len(newlist)):
    str = str + (newlist[i]) + " "
f.write(str)
f.close()

f = open("biba.txt", "r")
print(f.read())
import os

path = r"\\DANILA\Users\pokam\Desktop\My education\pp2\lab6"

if os.path.exists(path):
    for i in range (65, 91):
        os.remove(chr(i) + ".txt")
else:
    print("The file does not exist")
import os

path = r"\\DANILA\Users\pokam\Desktop\My education\pp2\lab6\test_folder\aldnk.txt"

if os.path.exists(path):
    f = open(path, "rt")
    print(f.read())
    b = open(path, "a")
    b.write("\nThats good! Enjoy the game :)")
    b.close()

    b = open(path, "r")
    print(b.read())

    q = open(path, "w")
    q.write("Woops! I have deleted the content!")
    q.close()

    q = open(path, "r")
    print(q.read())
    
else: 
    print("No")
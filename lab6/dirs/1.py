import os

path = r"\\DANILA\Users\pokam\Desktop\My education\pp2\lab6\test_folder"

with os.scandir(path) as it:
    for x in it:
        if(x.is_dir()):
            print(x.name)
print(" ")
with os.scandir(path) as it:
    for x in it:
        if(not x.is_dir()):
            print(x.name)
print(" ")
with os.scandir(path) as it:
    for x in it:
        print(x.name)
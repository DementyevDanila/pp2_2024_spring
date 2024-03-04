import os
path = r"\\DANILA\Users\pokam\Desktop\My education\pp2\lab6\test_folder\rtb.py"

if os.access(path, os.F_OK):
    print("File name:", os.path.basename(path))
    print("Diretory:", os.path.dirname(path))
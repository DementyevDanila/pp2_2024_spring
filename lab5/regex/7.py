import re

s = input()
txt = s.split('_')
for i in range(len(txt)):
    if i == 0:
        print(txt[i], end = "")
    else:
        txt[i] = txt[i].capitalize()
        print(txt[i], end = "")

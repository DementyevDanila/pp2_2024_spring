import re

s = input()
pattern = r"[,.\s]"
x = re.sub(pattern, ":", s)

print(x)
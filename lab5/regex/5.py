import re

s = input()
pattern = r"\w*a+b$"
x = re.findall(pattern, s)

print(x)
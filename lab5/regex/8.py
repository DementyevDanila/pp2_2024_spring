import re

s = input()
pattern = '[A-Z]{1}[a-z]*'
x = re.findall(pattern, s)

print(x)
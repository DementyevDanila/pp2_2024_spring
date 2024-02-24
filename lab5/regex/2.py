import re

s = input()
pattern = r"\w*ab{2,3}"
x = re.findall(pattern, s)

print(x)
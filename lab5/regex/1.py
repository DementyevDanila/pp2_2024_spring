import re

s = input()
pattern = r"\w*ab*\w+"
x = re.findall(pattern, s)

print(x)
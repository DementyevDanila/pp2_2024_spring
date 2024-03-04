s = list(input())

p = s.copy()
p.reverse()
print (p)
print (s)
if p == s:
    print("Palindrome!")
else:
    print("Not Palindrome :(")
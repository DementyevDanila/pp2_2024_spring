s = input()
upcnt = 0
lowcnt = 0
for x in s:
    if (ord(x) >= 65 and ord(x) <= 90):
        upcnt += 1
    if (ord(x) >= 97 and ord(x) <= 122):
        lowcnt += 1
print (upcnt)
print (lowcnt)
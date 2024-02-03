def spy(str):
    if (str.find("007") >= 0):
        return True
    else:
        return False

str = input()
str = str.split()
str2 = ""
str2 = "".join(str)

if spy(str2):
    print("True")
else:
    print("False")
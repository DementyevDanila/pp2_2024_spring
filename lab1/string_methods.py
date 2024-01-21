txt = "Magician"

x = txt.center(10) #string.center(length, character/(optional))
print(x) #method will center align the string, using a specified character (space is default) as the fill character.

txt = "I love apples, apple are my favorite fruit, Ryuk loves apples..."

x = txt.count("apple") #Return the number of times the value "apple" appears in the string
y = txt.count("apple", 10, 24) #Search from position 10 to 24
print(x, y)

txt = "Hello, welcome to my world."

x = txt.find("e") #first position where "e" is located
y = txt.find("e", 5, 10) #in interval  5 till 10
z = txt.find("nig") #if substring is not find, then value will be -1 
print(x, y, z)

txt = "Company12"

x = txt.isalnum() #method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
print(x) #there are same methods, like isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace(), istitle(), isupper()

txt = "Hello Sam!"

mytable = str.maketrans("S", "P")
print(txt.translate(mytable)) #method returns a mapping table that can be used with the translate() method to replace specified characters

x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y) # y is a string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
print(txt.translate(mytable)) 

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z) # z is a string describing which characters to remove from the original string.
print(txt.translate(mytable))

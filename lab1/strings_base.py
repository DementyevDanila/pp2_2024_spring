print("Hello")
print('Hello')
# "" and '' are the same in initialization

a = 'How are u?'
print(a)

#I can use """ or ''' to output multilne, the line breaks are inserted at the same position as in the code
a = """I'm fine, u?
 Same, do u wanna to go to cafe?
  Yes, wny no. But I don't have enough money...
   It doesn't matter, I will pay for u"""
print(a)

a = '''     I've always known, that u are the best!  
    Don't lie, I just have a bad day and want relax, so go to cafe.
   Okay, let's go ;)
'''
print(a)


#STRIINGS ARE ARRAYS

#Python does not have a character data type, a single character is simply a string with a length of 1.

a = "Hello, World!"
print(a[1])

#Looping Through a String

for x in "banana":
    print(x) #will print "banana" by symbols

a = "Hello my readers!"
print(len(a))

txt = "The best things in life are free!" #it's ike boolean expression,  if "true" is exist in txt - prog will print true
print("free" in txt)

txt = "The best things in life are free!"
print("freedom" in txt)

# If and boolean expressions

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
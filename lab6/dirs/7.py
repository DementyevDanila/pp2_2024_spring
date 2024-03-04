file1 = open('biba.txt', 'r')
file2 = open('biba_copy.txt', 'a')

for x in file1:
    file2.write(x)

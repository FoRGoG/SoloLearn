# file = open('newfile.txt', 'w')
# file.write('This has been written to a file')
# file.close()
#
# file = open('newfile.txt', 'r')
# print(file.read())
# file.close()

# file = open('newfile.txt', 'a')
#
# file.write('\nTHe Da Vinci Code')
# file.close()
#
# file = open('newfile.txt', 'r')
# print(file.read())
# file.close()


"""The write method returns the number of
bytes written to a file, if successful."""


# msg = 'Hello, world!'
# file = open('newfile.txt', 'w')
# amount_written = file.write(msg)
# print(amount_written)
# file.close()

"""Filling Up With Numbers

Take a number N as input and write the numbers 1 to N to 
the file "numbers.txt", each number on a separate line.

Sample Input
4

Sample Output
1
2
3
4

The given code reads the content of the file and outputs it.

You can use \n to make line breaks.

Do not forget to close the file after writing to it.
"""

n = int(input())

file = open("numbers.txt", "w+")
#your code goes here
for i in range(1, n+1):
    file.write(str(i) + '\n')
file.close()

f = open("numbers.txt", "r")
print(f.read())
f.close()

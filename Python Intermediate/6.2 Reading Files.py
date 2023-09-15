# file = open('/usercode/files/books.txt')
# cont = file.read()
# print(cont)
# file.close()


# file = open('/usercode/files/books.txt')
# print(file.read(5))
# print(file.read(7))
# print(file.read())
# file.close()


"""Calling the read() method without an argument 
will return the rest of the file content."""


# file = open('/usercode/files/books.txt')
#
# for line in file.readlines():
#     print(line)
#
# file.close()

# file = open('/usercode/files/books.txt')
#
# for line in file:
#     print(line)
#
# file.close()

"""Reading Files

You need to make a program to read
the given number of characters of a file.

Take a number N as input and output
the first N characters of the books.txt file.


The given code opens the books.txt file. 
Use the file object to read the content of the file. """

file = open("/usercode/files/books.txt")
#your code goes here
n = int(input())
print(file.read(n))

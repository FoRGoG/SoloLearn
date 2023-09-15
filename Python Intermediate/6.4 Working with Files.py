# try:
#     f = open("newfile.txt")
#     cont = f.read()
#     print(cont)
# finally:
#     f.close()

# """An alternaive way"""
#
# with open('newfile.txt') as f:
#     print(f.read())

"""Book Club

You are given a books.txt file, which includes book titles, each on a separate line.

Create a program to output how many words each title contains, in the following format:

Line 1: 3 words

Line 2: 5 words

...


Make sure to match the above mentioned format in the output.

To count the number of words in a given string,
you can use the split() function, or, alternatively,
count the number of spaces
(for example, if a string contains 2 spaces, then it contains 3 words).
"""

with open("newfile.txt") as f:
   lines = 0
   for i in f:
      lines += 1
      for x in range(1, lines+1):
         words = i.count(' ') + 1
      print('Line '+ str(x) + ': ' + str(words) + ' words')


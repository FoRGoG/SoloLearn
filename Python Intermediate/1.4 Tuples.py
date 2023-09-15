"""Contact Search

You are given a list of contacts, where each contact is represented by a tuple,
with the name and age of the contact.

Complete the program to get a string as input,
search for the name in the list of contacts and output the age of the contact in the format presented below:

Sample Input
John

Sample Output
John is 31

If the contact is not found, the program should output "Not Found"."""

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

result = input()
for i in contacts:
    if result in i:
        print(str(i[0]) + ' is ' + str(i[1]))
        break
else:
    print('Not Found')
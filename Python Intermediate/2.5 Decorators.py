"""Decorators"""

# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#     return wrap
#
# def print_text():
#     print("Hello world!")
#
# decorated = decor(print_text)
# decorated()
#
# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#     return wrap
#
# @decor
# def print_text():
#     print("Hello world!")
#
# print_text();

"""Collecting Reports

You are working on an invoicing system.

The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.

You need to add a decorator for the invoice() function, that will print the invoice in the following format:

Sample Input

42

Sample Output

***

INVOICE #42

***

END OF PAGE 

The given code takes the invoice number as input and passes it to the invoice() function."""

def decor(x):
    def star(num):
        print('***')
        x(num)
        print('***')
        print('END OF PAGE')
    return star

@decor
def star(num):
    print('INVOICE #' + num)

num = input()
star(num)
# num = 102
# if num > 100:
#     raise ValueError


# name = '123'
# raise NameError('Invalid name!')

"""Raising Exceptions

You are making a program to post tweets.
tweet must not exceed 42 characters.

Complete the program to raise an exception,
in case the length of the tweet is more than 42 characters.

You can use the len() function to calculate the length of the string."""


tweet = input()

try:
    if len(tweet) > 42:
        raise ValueError('It is too much!')
except:
    print("Error")
else:
    print("Posted")
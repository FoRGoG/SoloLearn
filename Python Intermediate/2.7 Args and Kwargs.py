# def function(named_arg, *args):
#     print(named_arg)
#     print(args)
#
# function(1, 2, 3, 4, 5)

# def my_func(x, y=7, *args, **kwargs):
#     print(kwargs)
#
# my_func(2, 3, 4, 5, 6, a=7, b=8)

"""Making It Work


The given code defined a function called my_min(),
which takes two arguments and returns the smaller one.

You need to improve the function,
so that it can take any number of variables, so that the function call works.

Remember, *args can be accessed inside the function as a tuple."""

def my_min(x, *y):
    y = sorted(y)
    if x < y[0]:
        return x
    else:
        return y[0]

print(my_min(8, 13, 4, 42, 120, 7))

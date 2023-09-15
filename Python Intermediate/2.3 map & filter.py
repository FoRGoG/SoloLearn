"""map"""
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

"""lambda map"""

nums = [11, 22, 33, 44, 55]
result = (list(map(lambda x: x +5, nums)))
print(result)

"""Getting A Raise!

You work on a payroll program.

Given a list of salaries, you need to take the bonus everybody 
is getting as input and increase all the salaries by that amount.

Output the resulting list.

You can use the map() function to increase all the values of the list."""

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input('Give me more salary here: '))

result = (list(map(lambda x: x + bonus, salaries)))
print(result)

"""filter"""

nums = [11, 22, 33, 44, 55]

result = (list(filter(lambda x: x%2==0, nums)))
print(result)
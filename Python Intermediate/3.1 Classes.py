# class Cat:
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs
#
# Jane = Cat('blue', 4)
# print(Jane.color)
# print(Jane.legs)

# class Dog:
#   def __init__(self, name, color):
#     self.name = name
#     self.color = color
#
#   def bark(self):
#     print("Woof!")
#
# arch = Dog('Arch', 'white')
# print(arch.name)
# arch.bark()

# Game Over
#
# You are making a video game!
# The given code declares a Player class,
# with its attributes and an intro() method.
#
# Complete the code to take the name and
# level from user input, create a Player object
# with the corresponding values and call the intro() method of that object.
#
# Sample Input
# Tony
# 12
#
#
# Sample Output
# Tony (Level 12)
# Use the dot syntax to call the intro() method for the declared object.

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + ' (Level ' + self.level + ')')

result1 = input()
result2 = input()
first = Player(result1, result2)
first.intro()
# """Class Methods"""
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     @classmethod
#     def new_square(cls, side_length):
#         return cls(side_length, side_length)
#
# square = Rectangle.new_square(5)
# print(square.calculate_area())
#
# """Static Methods"""
# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @staticmethod
#     def validate_topping(topping):
#         if topping == 'pineapple':
#             raise ValueError('No pineapples!')
#         else:
#             return True
# ingredients = ['cheese', 'onions', 'spam']
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)

"""Define The Methods

The given code takes 2 numbers as input
and calls the static area() method of the Shape class,
to output the area of the shape, which is equal to the height multiplied by the width.

To make the code work, you need to define the Shape class,
and the static area() method, which should return the multiplication of its two arguments.
Use the @staticmethod decorator to define a static method."""

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width * height


w = int(input())
h = int(input())

print(Shape.area(w, h))
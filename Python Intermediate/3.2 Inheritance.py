# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
# class Cat(Animal):
#     def purr(self):
#         print('Purr...')
#
# class Dog(Animal):
#     def bark(self):
#         print('Woof!')
#
# fido =Dog('Fido', 'brown')
# print(fido.color)
# fido.bark()

# class Wolf:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def bark(self):
#         print('Grr...')
#
# class Dog(Wolf):
#     def bark(self):
#         print('Woof')
#
# husky = Dog('Max', 'grey')
# husky.bark()

# class A:
#     def spam(self):
#         print(1)
#
# class B(A):
#     def spam(self):
#         print(2)
#         super().spam()
#
# B().spam()

"""Fine Art

You are making a drawing application,
which has a Shape base class.

The given code defines a Rectangle class,
creates a Rectangle object and calls its area() and perimeter() methods.

Do the following to complete the program:

1. Inherit the Rectangle class from Shape.

2. Define the perimeter() method in the Rectangle class,
printing the perimeter of the rectangle. """

class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width * self.height)

class Rectangle(Shape):
    def perimetr(self):
        print(2*(self.width + self.height))


result1 = int(input())
result2 = int(input())
finish = Rectangle(result1, result2)
finish.area()
finish.perimetr()

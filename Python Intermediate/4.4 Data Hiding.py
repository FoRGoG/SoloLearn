# class Queue:
#     def __init__(self, contents):
#         self._hiddenlist = list(contents)
#
#     def push(self, value):
#         self._hiddenlist.insert(0, value)
#
#     def pop(self):
#         return self._hiddenlist.pop(-1)
#
#     def __repr__(self):
#         return "Queue({})".format(self._hiddenlist)
#
# queue = Queue([1, 2, 3])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue._hiddenlist)

# class Spam:
#     __egg = 7
#     def print_egg(self):
#         print(self.__egg)
#
# s = Spam()
# s.print_egg()
# print(s._Spam__egg)
# print(s.__egg)

"""Preservation

We are working on a game. Our Player class has name and private _lives attributes.
The hit() method should decrease the lives of the player by 1.
In case the lives equal to 0, it should output "Game Over".
Complete the hit() method to make the program work as expected.

The code creates a Player object and calls its hit() method multiple times."""

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print('Game Over')

p = Player('Cyberpank77', 3)
p.hit()
p.hit()
p.hit()
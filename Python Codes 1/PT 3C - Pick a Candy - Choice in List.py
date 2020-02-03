# Pick a candy
# In this exercise, you will write a program to randomly select a candy from a box.
# [ ] Complete the function `pick_candy` so it returns a candy from box at random
from random import choice


def pick_candy():
    box = ["Taffy", "Brownie", "Cookie", "Candy bar", "Chocolate", "Lollipop", "Gingerbread", "Marshmallow"]
    return choice(box)


print(pick_candy())
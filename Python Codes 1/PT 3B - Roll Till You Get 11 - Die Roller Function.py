# Die Roller - Roll till you get 11: Practice Task 3B
# In this exercise, you will count the number of times you need to roll a set of 2 dice till you get a roll sum of 11.
from random import randint


def die_roller():
    return randint(1, 6)


def roll_sum():
    return die_roller() + die_roller()


x = roll_sum()
count = 1
while x != 11:
    x = roll_sum()
    count += 1
print("No. of times needed to get a roll sum of 11 is: ", count)

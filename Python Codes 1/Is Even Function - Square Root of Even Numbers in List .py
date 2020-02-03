# Square Root of Even Numbers in a List
import math


def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False


# [ ] Use the function is_even to print the square root of all the even numbers in the following list
l = [25, 34, 193, 2, 81, 26, 44]

for num in l:
    if is_even(num):
        print(math.sqrt(num))


# Even or Odd Function

# [ ] Fill out the function is_even with a code block that returns True if n is even and returns False if n is odd
import math


def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False


# Test the function
x = 5
if is_even(x):
    print("Number is even")
else:
    print("Number is odd")








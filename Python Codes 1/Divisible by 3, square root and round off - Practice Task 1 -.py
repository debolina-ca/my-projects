# Practice Task 1 - divisible by 3, square root and round off
# Write a program to:
# 1) find all the numbers in a list that are divisible by 3
# 2) display the square root of these numbers
# 3) use a rounding function to display the square roots while ignoring the decimal fraction
import math
lst = [23, 45, 65, 2345, 42, 76, 37, 87, 647, 35, 37, 39, 898, 92, 18]
new_lst = []
for num in lst:
    print("Number in given list is: ", num)
    if num % 3 == 0:
        num = math.sqrt(num)
        print("Square root of number that is divisible by 3 is: ", num)
        num = math.trunc(num)
        new_lst += [num]
        print("Round off value of the number is: ", num)
print("New list of the numbers: ", new_lst)

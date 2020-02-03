# Reverse a string using while, .pop(), insert()
# pop() the first item in the list and add to the beginning of a new string that will be reversed
some_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77]
print(some_numbers)
reverse_string = [some_numbers[-1]]
while some_numbers:
    new_num = some_numbers.pop()
    reverse_string.insert(-1, new_num)
reverse_string.pop()
print(reverse_string)

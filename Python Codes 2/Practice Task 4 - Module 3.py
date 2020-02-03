# Task 4 - combine lists with + and .extend()

# [ ] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# pythonic casting of a range into a list
numbers_2 = list(range(30,50,2))
print("numbers_1:",numbers_1)
print("numbers_2",numbers_2)
print(numbers_1 + numbers_2)

# [ ] print the combined element lists (first_row & second_row) using ".extend()" method
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
print("1st Row:", first_row)
print("2nd Row:", second_row)
first_row.extend(second_row)
print(first_row)

# Project: Combine 3 element rows - Choose to use "+" or ".extend()" to build output similar to
# combined 3 element rows
elem_1 = ['Hydrogen', 'Helium']
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
print(elem_1 + elem_2 +elem_3)

# [ ] .extend() jack_jill with "next_line" string - print the result
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']
jack_jill.extend(next_line)
print(jack_jill)

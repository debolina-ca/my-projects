# Task 3 - iteration with range(start:stop:skip)
# [ ] create a list of odd numbers (odd_nums) from 1 to 25 using range(start,stop,skip)
# [ ] print odd_nums
# hint: odd numbers are 2 digits apart
odd_nums = []
for num in range(1, 26, 2):
    odd_nums += [num]
print(odd_nums)

# [ ] create a Decending list of odd numbers (odd_nums) from 25 to 1 using range(start,stop,skip)
# [ ] print odd_nums,  output should resemble [25, 23, ...]
odd_nums = []
for num in range(25, 0, -2):
    odd_nums += [num]
print(odd_nums)

# the list, elements, contains the names of the first 20 elements in atomic number order
# [ ] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
for index in range(1, len(elements), 2):
    print(index+1, " - ", elements[index])

# [ ] the list, elements_40, contains the names of the first 40 elements in atomic number order
# [ ] print the odd number elements "1 - Hydrogen, 3 - Lithium,.." in the list with the atomic number elements_40
elements_40 = ['Hydrogen', \
 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', \
 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', \
 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', \
 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']
for index in range(0, len(elements_40), 2):
    print(index+1, "-", elements_40[index])

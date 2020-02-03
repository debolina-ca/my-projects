# Task 5 - .reverse() : reverse a list in place


# use .reverse() to print elements starting with "Calcium", "Chlorine",... in reverse order
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
elements.reverse()
print(elements)


# [ ] reverse order of the list... Then print only words that are 8 characters or longer from the now reversed order
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
spell_list.reverse()
print(spell_list)
for item in spell_list:
    if len(item) >= 8:
        print(item)

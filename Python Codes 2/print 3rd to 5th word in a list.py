# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spell_list
# output should include "February", "November", "Annual"
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for item in range(2, 5):
    print(spell_list[item])

# [ ] using code find the index of "Annual" in spell_list
# [ ] using range, print the spell_list including "Annual" to end of list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for item in range(7):
    if spell_list[item] == "Annual":
        print("Index of 'Annual' is: ", item)
spell_list.remove("Annual")
spell_list.append("Annual")
print(spell_list)



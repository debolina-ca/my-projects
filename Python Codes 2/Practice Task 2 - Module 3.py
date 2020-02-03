# Task 2 - iteration with range(start) & range(start,stop)

# [ ] using range() print "hello" 4 times
for index in range(4):
    print("hello")


# [ ] find spell_list length
# [ ] use range() to iterate each half of spell_list
# [ ] label & print the first and second halves
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
length = len(spell_list)
mid = int(length/2)
first_half = []
second_half = []
for index in range(mid):
    first_half += [spell_list[index]]
for index in range(mid, length):
    second_half += [spell_list[index]]
print(first_half)
print(second_half)

# [ ] build a list of numbers from 20 to 29: twenties
# append each number to twenties list using range(start,stop) iteration
# [ ] print twenties
# [ ] iterate through the numbers populated in the list twenties and add each number to a variable: total
# [ ] print total
twenties = []
total = 0
for num in range(20, 30):
    twenties += [num]
    total += num
print(twenties)
print("Total: ", total)

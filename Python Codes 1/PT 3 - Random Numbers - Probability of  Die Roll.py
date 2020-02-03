# Random numbers - Probability of a die roll: Practice Task 3
# It is possible to mathematically predict the probability (or chance) of getting a certain die roll;
# however, in this exercise you will use Python to do it without math.
# The trick is to roll a die a large number of times and count how many times we get a certain roll.
# You can, then, divide the count by the large number to get the probability.
# For a fair 6-sided die, the chance of getting any of its faces is about 16.6%

# [ ] Complete the following program to display the probability of a certain die roll

from random import randint


def die_roller():
    return randint(1, 6)


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for count in range(100000):
    x = die_roller()
    if x == 1:
        one += 1
    elif x == 2:
        two += 1
    elif x == 3:
        three += 1
    elif x == 4:
        four += 1
    elif x == 5:
        five += 1
    else:
        six += 1
die_val = int(input("Enter the side of a die roller to predict its probability (1 - 6): "))
while die_val > 6 or die_val <1:
    print("Wrong input!")
    die_val = int(input("Enter the side of a die roller to predict its probability (1 - 6): "))
val = 0
if die_val == 1:
    val = one
elif die_val == 2:
    val = two
elif die_val == 3:
    val = three
elif die_val == 4:
    val = four
elif die_val == 5:
    val = five
elif die_val == 6:
    val = six
else:
    pass
print("Probability of getting", die_val, "in a die roller is: ", round((val/100000)*100, 2), "%")

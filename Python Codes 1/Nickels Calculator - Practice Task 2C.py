# Nickels Calculator
# [ ] Complete the function `nickels_count` so it calculates and prints the number of nickels in `input_cents`
# The function input `input_cents` should be in cents
# The function should print the number of calculated nickels in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 5, why?)
# HINT: You might want to use % and // operators

import math


def nickels_count(input_cents):
    rem_cents = input_cents % 5
    nickels = input_cents // 5
    return nickels



# test with $2
# Output should be: 40 nickel\s
dollars = 2
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)
print(remaining_cents, "nickel\s")

# test with $5.30
# Output should be: 106.0 nickel\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)
print(remaining_cents, "nickel\s")

# test with $9.49
# Output should be: 189.0 nickel\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)
print(remaining_cents, "nickel\s")
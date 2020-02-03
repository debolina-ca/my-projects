# Dimes
# [ ] Complete the function `dimes_count` so it calculates and prints the number of dimes in `input_cents`
# The function input `input_cents` should be in cents
# The function should print the number of calculated dimes in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 10, why?)
# HINT: You might want to use % and // operators

import math


def dimes_count(input_cents):
    rem_cents = input_cents % 10
    dimes = input_cents // 10
    return dimes


# test with $2
# Output should be: 20 dime\s
dollars = 2
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)
print(remaining_cents, "dime\s")


# test with $5.30
# Output should be: 53.0 dime\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)
print(remaining_cents, "dime\s")

# test with $9.49
# Output should be: 94.0 dime\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)
print(remaining_cents, "dime\s")
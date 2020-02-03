# COIN CALCULATORS - Practice Task 2 using Mathematical Operators
# Develop functions to count the number of coins in a certain dollar amount and then
# write a program that can calculate the change due to a customer in coins

# [ ] Complete the function `quarters_count` so it calculates and prints the number of quarters in `input_cents`
# The function input `input_cents` should be in cents
# The function should print the number of calculated quarters in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 25, why?)
# HINT: You might want to use % and // operators

import math


def quarters_count(input_cents):
    rem_cents = input_cents % 25
    quarters = input_cents//25
    return quarters


# test with $2
# Output should be: 8 quarter\s
dollars = 2
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)
print(remaining_cents, "quarter\s")

# test with $5.30
# Output should be: 21.0 quarter\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)
print(remaining_cents, "quarter\s")

# test with $9.49
# Output should be: 37.0 quarter\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)
print(remaining_cents, "quarter\s")
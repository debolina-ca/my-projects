# Change Calculator
# [ ] Complete the function `coins_due` to calculate and print the change due to a customer in coins
#
# The function `coins_due` has 2 inputs:
#      - `amount_paid`: Amount paid by a customer (in cents)
#      - `item_price`: Purchase price of an item
#
# The function should print:
#      - The number of quarters due
#      - The number of dimes due
#      - The number of nickels due
#      - The number of cents due
#
# The function does not need to return anything
#
# HINT: Use the functions you developed before `quarters_count`, `dimes_count`, `nickels_count`

import math


def quarters_count(input_cents):
    rem_cents = input_cents % 25
    quarters = input_cents // 25
    return quarters


def dimes_count(input_cents):
    rem_cents = input_cents % 10
    dimes = input_cents // 10
    return dimes


def nickels_count(input_cents):
    rem_cents = input_cents % 5
    nickels = input_cents // 5
    return nickels


def coins_due(amount_paid, item_price):
    print("Change due:")
    change_due = (amount_paid - item_price) * 100
    quarters1 = quarters_count(change_due)
    print("The number of quarters due: ", quarters1, "quarter\s")
    change_due = change_due - quarters1 * 25
    dimes1 = dimes_count(change_due)
    print("The number of dimes due: ", dimes1, "dime\s")
    change_due = change_due - dimes1 * 10
    nickels1 = nickels_count(change_due)
    print("The number of cents due: ", nickels1, "nickel\s")
    change_due = change_due - nickels1 * 5
    print("The number of cents due: ", change_due, "cents")


amount_paid1 = float(input("Enter amount paid by customer in dollars: "))
item_price1 = float(input("Enter purchase price of the item in dollars: "))
coins_due(amount_paid1, item_price1)

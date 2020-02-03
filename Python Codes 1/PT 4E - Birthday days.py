# Practice Task 4E: Birthday days
# Write a program to display a list of all your birthdays from the day you were born till 2025.
# You should also show the weekdays so you can see which of them was (or will be) on a weekend
from datetime import datetime
for yr in range(1985, 2026):
    birthday = datetime(month = 4, day = 5, year = yr)
    print(birthday.strftime("%A, %d %B, %Y"))
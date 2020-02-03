# Practice Task 5C: Complete the program below to find out if July 4th is within 10 days of today's date,
# if it is, find out if has passed or not
from datetime import datetime
import math
# get today's date
todays_date = datetime.today()

# 4th of July of current year
july_4th = datetime(month=7, day=4, year=todays_date.year)
days_difference = todays_date - july_4th
days_difference = days_difference.days
if days_difference < 0 and math.fabs(days_difference) <= 10:
    print("July 4th is within 10 days of today's dat and the day has not passed")
elif days_difference > 0 and math.fabs(days_difference) <= 10:
    print("July 4th is within 10 days of today's dat and the day has passed")
elif days_difference < 0 and math.fabs(days_difference) > 10:
    print("July 4th is not within 10 days of today's dat and the day has not passed")
elif days_difference == 0:
    print("Today is 4th July")
else:
    print("July 4th is not within 10 days of today's dat and the day has passed")

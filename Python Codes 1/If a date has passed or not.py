# Write a program to find out if 4th of July of this year has passed or not
from datetime import date
date_1 = date.today()
date_2 = date(year = 2019, month = 7, day = 4)
if date_1 > date_2:
    print("4th July has passed this year by", (date_1 - date_2), "days")
elif date_1 < date_2:
    print("4th July is yet to come this year by", (date_2 - date_1), "days")
else:
    print("Today is the 4th of July 2019")

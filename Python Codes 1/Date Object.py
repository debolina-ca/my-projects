# Date Object
from datetime import date

# assign a date
SomeDate = date(year = 2015, day = 28, month = 2)
print("Old date: ", SomeDate)

# modify year and day
# 2016 is a leap year, so we can set the date to Feb 29 2016
SomeDate = SomeDate.replace(year = 2016, day = 29)
print("New date: ", SomeDate)

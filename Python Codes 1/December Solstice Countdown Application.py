# Creating a December Solstice Countdown Application
from datetime import datetime, timedelta
now = datetime(day = 15, month = 6, year = 2019)
solstice = datetime(day = 21, month = 12, year = 1)
solstice = solstice.replace(year = now.year)
count = solstice - now
print("count is type", type(count))
if solstice >= now:
    print("There are only", count.days, "days till December solstice")
else:
    print("December solstice has passed this year")
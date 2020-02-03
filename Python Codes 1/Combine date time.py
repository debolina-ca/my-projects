# Combining separate date and time objects into a datetime object

from datetime import datetime, time, date

# assign a time object
t = time(hour = 6, minute = 45, second = 0)

# assign a date object
d = date.today()

# combine t and d into a datetime object
dt = datetime.combine(date = d, time = t)

print(dt)

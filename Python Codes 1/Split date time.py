# Splitting a datetime object into separate date and time objects

from datetime import datetime, time, date

# get today's date and current local time
dt = datetime.today()

# split into time t and date d
t = dt.time()
print("Time is: ", t)

d = dt.date()
print("Date is: ", d)

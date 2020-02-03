# Time Delta Objects - dt
# Use a `timedelta` object to find out how many days are left until your upcoming birthday
from datetime import timedelta, datetime
date_2 = datetime.today()
date_1 = datetime(year = 2020, month = 4, day = 5)
delta_2 = date_1 - date_2
print(delta_2)
seconds = delta_2.total_seconds()
print(seconds)

# Get the stored attributes
d = delta_2.days
s = delta_2.seconds
ms = delta_2.microseconds
print("Days = ", d, "| Seconds = ", s, "| Microseconds = ", ms)

from datetime import timedelta
delta1 = timedelta(days = 7,  hours = 2)
print(delta1)

# Formatting time objects

from datetime import time
t = time(hour = 10, minute = 15)

# display as 10:15 AM
# string passed to strftim includes all necessary spaces and semicolons
formatted_string = t.strftime("%I:%M %p")
print("First format: ", formatted_string)

# display as 10:15:00 (24 hour clock, no AM/PM)
formatted_string = t.strftime("%H:%M:%S")
print("Second format: ",formatted_string)

# Formatting date objects

from datetime import date
d = date(year = 1999, month = 11, day =3)

# display as November, 03, 1999
# string passed to strftime includes all necessary spaces and commas
formatted_string = d.strftime("%B, %d, %Y")
print("First format: ", formatted_string)

# display as Nov 03 99
formatted_string = d.strftime("%b %d %y")
print("Second format: ", formatted_string)

# Formatting datetime objects

from datetime import datetime
dt = datetime(year = 1999, month = 11, day = 3, hour = 10, minute = 15)

# display as November, 03, 1999 @ 10:15 AM
formatted_string = dt.strftime("%B, %d, %Y @ %I:%M %p")
print("First format: ", formatted_string)

# display as Nov 03 99 / 10:15:00
formatted_string = dt.strftime("%b %d %y / %H:%M:%S")
print("Second format: ", formatted_string)

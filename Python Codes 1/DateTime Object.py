# Assigning a datetime object

from datetime import datetime

# July 4th 2022, at 4:30 PM

# Method 1
dt = datetime(2022, 7, 4, 16, 30)
print("Method 1: ", dt)

# Method 2
dt = datetime(day = 4, month = 7, year = 2022, minute = 30, hour = 16)
print("Method 2: ", dt)


# Getting a datetime attribute

from datetime import datetime

# July 4th 2022, at 4:30 PM
dt = datetime(2022, 7, 4, 16, 30)

# access year
print("Year is: ", dt.year)

# access minute
print("Minute is: ", dt.minute)

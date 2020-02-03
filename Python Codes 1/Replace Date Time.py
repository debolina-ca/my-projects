# Modifying the attributes of an assigned datetime object

from datetime import datetime

# July 4th 2022, at 4:30 PM
dt = datetime(2022, 7, 4, 16, 30)

# change year to 2020 and second to 30
dt = dt.replace(year = 2020, second = 30)
print(dt)

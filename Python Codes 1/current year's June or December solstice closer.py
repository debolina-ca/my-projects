# Find out if you are closer to the current year's June or December solstice
from datetime import datetime, timedelta
import math
now = datetime.today()
december_solstice = datetime(month = 12, day = 21, year = now.year)
june_solstice = datetime(month = 6, day = 21, year = now.year)
time_to_jun = june_solstice - now
time_jun = time_to_jun.days
time_jun = math.fabs(time_jun)
time_to_dec = december_solstice - now
time_dec = time_to_dec.days
time_dec = math.fabs(time_dec)
print("June: ", time_jun)
print("December: ", time_dec)
if time_jun < time_dec:
    print("June solstice is closer")
elif time_jun > time_dec:
    print("December solstice is closer")
else:
    print("Both are equally close, and is", time_jun, "days before and after from today")

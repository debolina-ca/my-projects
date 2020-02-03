# Comparing datetime objects
from datetime import date
birthday1 = date(year = 1981, month = 11, day = 21)
birthday2 = date(year = 1985, month = 4, day = 5)
if birthday1 > birthday2:
    print("Debolina is older")
elif birthday1 < birthday2:
    print("Nabin is older")
else:
    print("Nabin and Debolina are of the same age")
    
# Practice Task 4D: American VS European date format: In the United States, the date is formatted as Month/Day/Year;
# whereas, in Europe the date is formatted as Day/Month/Year.
# Write two functions that will display a datetime object in the American or European format

# [ ] Complete the functions `american_format(d)` and `european_format(d)` to display the
# datetime object d in the proper format
from datetime import datetime


def american_format(d):
    return d.strftime("%m/%d/%Y")


def european_format(d):
    return d.strftime("%d/%m/%Y")


# test
d = datetime(month=6, year=2019, day=19)

print("American format:", american_format(d))
print("European format:", european_format(d))

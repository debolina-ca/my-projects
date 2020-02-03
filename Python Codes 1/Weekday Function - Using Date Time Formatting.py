# Weekday Function - Date Time Formatting
# [ ] Complete the function `weekday` to return the weekday name of `some_date`
# Use the function to find the weekday on which you were born

from datetime import date


def weekday(some_date):
    formatted_string = some_date.strftime("%A")
    return formatted_string


# Modify to your birthdate
bd = date(day=5, month=4, year=1985)

# Display the day on which you were born
day = weekday(bd)
print(day)




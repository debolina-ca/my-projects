# Practice Task 4C: Write a program that displays the current date as (Friday, December 15, 2017)
from datetime import datetime
dt = datetime.today()
formatted_string = dt.strftime("%A, %B %d, %Y")
print(formatted_string)

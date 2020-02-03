# Practice Task 4A: Write a program that displays the current time as (HH:MM AM/PM) (example 02:28 PM)
from datetime import datetime
t = datetime.today()
formatted_string = t.strftime("%I:%M %p")
print(formatted_string)




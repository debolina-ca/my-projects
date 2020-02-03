# Practice Task 4B: Write a program that displays the current time as (HH:MM:SS) (example 14:28:10)
from datetime import datetime
t = datetime.today()
formatted_string = t.strftime("%H:%M:%S")
print(formatted_string)




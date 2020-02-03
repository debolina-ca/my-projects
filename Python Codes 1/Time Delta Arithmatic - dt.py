# Time Delta Arithmatic
from datetime import datetime, timedelta
days_100 = timedelta(days = 100)
current_date = datetime.today()
new_date = current_date + days_100
print("After 100 days: ", new_date.strftime("%b-%d-%Y"))

# Create a `time` variable containing the time: 8:45:01:000150 PM
from datetime import time
t = time(20, 45, 1, 150)
print(t)

#  Modify t3 to: 4:10 PM
from datetime import time
t3 = time(hour = 15, minute = 10, second = 0)
t3 = t3.replace(hour = 16)
print(t3)



# Float Error Rounding
# [ ] Use an appropriate rounding function to fix the following `float` error
from math import ceil
# Price of a chocolate box
p = 4.35

# Quantity needed
q = 200

# Order total price (Should be 4.35 * 200 = $870.00)
total = p * q

print("Total price: ", ceil(total))



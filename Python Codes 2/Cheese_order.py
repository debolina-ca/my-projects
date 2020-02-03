# Cheese Order - Module 3 Required Coding Activity
order_amount = float(input("Enter cheese order weight in kg (numeric value): "))
price_per_kg = 50
max_order = 100
min_order = 0.25
if order_amount > 100:
    print(order_amount, "is more than currently available stock")
elif order_amount < 0.25:
    print(order_amount, "is below minimum order amount")
else:
    print(order_amount, "costs $" + str(price_per_kg*order_amount))

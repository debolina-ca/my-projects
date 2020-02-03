# Cash Register Total
subtotal = 0
purchase_amounts = []
item_price = input('Enter price of items or "done" to exit: ')
while True:
    if item_price.lower() == "done":
        break
    else:
        purchase_amounts.append(item_price)
        item_price = input('Enter price of items or "done" to exit: ')
print(purchase_amounts)
while purchase_amounts:
    subtotal = subtotal + float(purchase_amounts.pop())
print(subtotal)




# SHIRT SALE
size = input("Enter the size of shirt (S, M, L): ")
if size.upper() == "S":
    print("Small = $6")
elif size.upper() == "M":
    print("Medium = $7")
elif size.upper() == "L":
    print("Large = $8")
else:
    print(size, "not available")

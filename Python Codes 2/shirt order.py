# Shirt Order
shirt_color = input("enter your choice of color for the shirt (White or Blue): ")
shirt_size = input("enter your size for shirt (L, M, S): ")
available = False
if shirt_color.lower() == "white":
    if shirt_size.upper() == "L":
        available = True
    elif shirt_size.upper() == "M":
        available = True
    elif shirt_size.upper() == "S":
        available = False
    else:
        print("invalid size entered")
elif shirt_color.lower() == "blue":
    if shirt_size.upper() == "M":
        available = True
    elif shirt_size.upper() == "S":
        available = True
    elif shirt_size.upper() == "L":
        available = False
    else:
        print("invalid size entered")
else:
    print("invalid color entered")
if available == True:
    print("available")
    print("Your order for the shirt is confirmed for color", shirt_color, "and size", shirt_size)
else:
    print("unavailable")

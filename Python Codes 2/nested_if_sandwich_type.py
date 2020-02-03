sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
if sandwich_type.lower() == "c":
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    elif cheese_type.lower() == "m":
        print("Here is your Manchego cheese sandwich")
    else:
        print("Sorry, we don't have", cheese_type, "choice today.")
elif sandwich_type.lower() == "v":
    print("Here is your Veggie Special. Thank you.")
else:
    print("Sorry, we don't have", sandwich_type, "choice today.")

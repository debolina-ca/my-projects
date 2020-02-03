# Shirt Count and Shirt Register
shirt_count = 0
shirt_size = ""
small = 0
medium = 0
large = 0
small_size_price = 6
medium_size_price = 7
large_size_price = 8
total_small_price = 0
total_medium_price = 0
total_large_price = 0
total_price = 0
while True:
    shirt_size = input("Enter the size of shirt (S, M, L) or enter exit to exit the program: ")
    if shirt_size.lower() == "exit":
        print()
        break
    elif shirt_size.upper() == "S":
        small += 1

    elif shirt_size.upper() == "M":
        medium += 1

    elif shirt_size.upper() == "L":
        large += 1

    else:
        print("Not a valid size: Counted as a medium shirt size M")
        medium += 1
    shirt_count += 1
total_small_price = small*small_size_price
total_medium_price = medium*medium_size_price
total_large_price = large*large_size_price

total_price = total_small_price + total_medium_price + total_large_price
print("Total shirts = ", shirt_count, "\nSmall shirts = ", small, "\nMedium shirts = ", medium, "\nLarge shirts = ", large)
print("Total shirt price = ", total_price, "\nTotal Small S size price = ", total_small_price, "\nTotal Medium M size price = ", total_medium_price, "\nTotal Large L size price = ", total_large_price)



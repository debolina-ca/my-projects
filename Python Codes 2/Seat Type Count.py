# Seat Type Count

# initilize variables
seat_count = 0
soft_seats = 0
hard_seats = 0
num_seats = 4

# loops tallying seats using soft pads vs hard, until seats full or user "exits"
while True:
    seat_type = input("Enter seat type \"soft\" or \"hard\" or enter \"exit\" to finish: ")
    if seat_type.lower() == "exit":
        print()
        break
    elif seat_type.lower() == "hard":
        hard_seats += 1
    elif seat_type.lower() == "soft":
        soft_seats += 1
    else:
        print("invalid entry: counted as hard")
        hard_seats += 1
    seat_count += 1
    if seat_count >= num_seats:
        print ("Seats are full")
        break
print("Seats total: ", seat_count,"\nHard seats: ", hard_seats, "\nSoft seats: ", soft_seats)


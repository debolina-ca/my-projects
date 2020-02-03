# [ ] review the code, run, fix the error
tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
        # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("you win!")
        break
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))
print("Game ended")
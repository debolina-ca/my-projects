# Use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
count = 4
while count > 0:
    color_guess = input("Enter a color of rainbow: \n")
    if color_guess.lower() in rainbow_colors:
        print("Yes", color_guess, "is a rainbow color")
        break
    else:
        print(color_guess, "is incorrect")
    count = count - 1





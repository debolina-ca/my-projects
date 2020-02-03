# Number Guess
number_guess = "0"
secret_number = "5"
while True:
    number_guess = input("guess a number between 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess, "is correct!\n")
        break
    else:
        print(number_guess, "is incorrect\n")

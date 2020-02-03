def letter_guess(guess, answer="e"):
    count = 1
    while count <= 3:

        if guess == answer:
            return("Correct", guess == answer)
        if guess != answer:
            print("Incorrect, try again", guess == answer)
        count = count + 1
guess_user = input("Enter a letter (a-z): ")
letter_guess(guess_user)



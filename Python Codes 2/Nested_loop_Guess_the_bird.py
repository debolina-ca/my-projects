# Guess the Bird - 3 guesses
bird_names = ("parrot", "eagle", "crow", "peacock", "sparrow")
bird_guess = input("Guess name of a bird: ")
if bird_guess.lower() in bird_names:
    print("Yes, 1st try!")
else:
    bird_guess = input("No, that's not right! Guess again, the name of a bird: ")
    if bird_guess.lower() in bird_names:
        print("Yes, 2nd try!")
    else:
        bird_guess = input("No, that's not right! Guess again, the name of a bird. This is your third and last chance: ")
        if bird_guess.lower() in bird_names:
            print("Yes, 3rd try!")
        else:
            print("Sorry you have exhausted all 3 guesses...")



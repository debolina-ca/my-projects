# Guessing a letter A-Z
def check_guess(letter, guess):
    if guess.isalpha()== False:
        print("Invalid guess. ", guess, "is ", guess.isalpha())
    elif guess.lower() == letter:
        print(guess.lower() == letter, guess, "is correct")
    elif guess.lower() > letter:
        print(guess.lower() == letter, guess, "is high")
    elif guess.lower() < letter:
        print(guess.lower() == letter, guess, "is low")
test_letter = "k"
test_guess = input("enter a single alphabet (a - z): ")
check_guess(test_letter, test_guess)




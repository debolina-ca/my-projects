# Random Pi Guessing
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt
pi_file = open('pi.txt', 'r')
name = input("Enter your name: ")
print("hi", name)
seed = len(name)
pi_file.seek(seed)
pi_digits = pi_file.read()
print(pi_digits)
digit = pi_file.read(1)
correct = 0
wrong = 0
guess = input("enter a single digit guess or 'q' to quit: ")
while guess.isdigit():
    if digit == ".":
        digit = pi_file.read(1)
    elif digit == "\n":
        seed += 1
        pi_file.seek(seed)
        digit = pi_file.read(1)
    elif guess == digit:
            print("Correct")
            correct += 1
    else:
        print("Incorrect")
        wrong += 1
    guess = input("enter a single digit guess or 'q' to quit: ")
print("Correct", correct, "\nIncorrect", wrong)


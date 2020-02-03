# Practice Task 1 - Module 4: Order the Rainbow
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
rainbow_file = open('rainbow.txt', 'r')
rainbow_colors = rainbow_file.readlines()
rainbow_colors.sort()
for item in rainbow_colors:
    print(item)

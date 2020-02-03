# Rainbow Colors - Readline and while loop
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
rainbow_file = open('rainbow.txt', 'r')
color = rainbow_file.readline()
while color:
    print(color.upper())
    color = rainbow_file.readline()
rainbow_file.close()

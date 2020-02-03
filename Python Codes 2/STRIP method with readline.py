# .strip() with arguments
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities_messy -o cities_messy.txt
cities_messy = open('cities_messy.txt', 'r')
print(cities_messy)
line = cities_messy.readline().strip(':\n ')
while line:
    print(line)
    line = cities_messy.readline().strip(':\n ')
cities_messy.close()

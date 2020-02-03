# .readlines() -  open the cities file as a list
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()
for line in cities_lines:
    print(line)

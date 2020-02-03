# Print the cities that start with the letter "D" or greater
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()
for city in cities_lines:
    if city >=  "D":
        print(city)
cities_file.close()

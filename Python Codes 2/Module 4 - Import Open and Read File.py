# Curl Command for Azure

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', 'r')
cities_file
cities = cities_file.read()
cities
print(cities)

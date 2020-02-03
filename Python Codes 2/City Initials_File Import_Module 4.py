# City Initials
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', "r")
cities = cities_file.read()
initials = ""
for letter in cities:
    if letter.isupper():
        initials += letter
    elif letter == "\n":
        initials += letter
print(initials)

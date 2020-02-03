# [ ] print cites from visited_cities list in alphbetical order using .sort()
# [ ] only print cities that names start "Q" or earlier
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
visited_cities.sort()
print(visited_cities)
length = len(visited_cities)
for index in range(length):
    if visited_cities[index].upper() <= "Q":
        print(visited_cities[index])

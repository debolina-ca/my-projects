# [ ] make a sorted copy (sorted_cities) of visited_cities list
# [ ] remove city names 5 characters or less from sorted_cities
# [ ] print visited cites and sorted cities
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
sorted_cities = []
print(visited_cities)
length = len(visited_cities)
for index in range(length):
    city = visited_cities[index]
    length_city = len(city)
    if length_city > 5:
        sorted_cities += [visited_cities[index]]
sorted_cities = sorted(sorted_cities)
print(sorted_cities)

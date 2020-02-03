cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search_letter = "a"
total = 0
for city_name in cities:
    total += city_name.lower().count("a")
print("No. of 'a's in the list is", total)

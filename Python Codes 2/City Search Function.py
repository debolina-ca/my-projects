# City Search Function
def city_search(search_item, cities = ["New York", "Shanghai", "Munich", "Tokyo"]):
    for city in cities:
        if city.lower() == search_item.lower():
            return True
        else:
            pass
    return False


visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search = input("enter a city visited: ")
print()
print(search.title(), "in default cities is", city_search(search))
print(search.title(), "in visited_cities list is", city_search(search, visited_cities))

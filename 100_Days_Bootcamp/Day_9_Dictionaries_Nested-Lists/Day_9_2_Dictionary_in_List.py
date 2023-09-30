# You are going to write a program that adds to a 'travel_log', which is a list containing 2 dictionaries.
# Write a function that will word with the following line of code to add the entry for Russia to the 'travel_log'.
#   add_new_country("Russia", 2, ["Moscow", "Saint Petersburg", "Vologograd"])

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
    
},
{   
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgar"]
},
]

# --- My answer ---
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {
    "country": country_visited,
    "visits": times_visited,
    "cities": cities_visited,
}
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg", "Vologograd"])
print(travel_log)


# --- Teacher's answer ---
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
countries = input().split(", ")
capitals = input().split(", ")

dict_of_capitals = dict(zip(countries, capitals))

for country, capital in dict_of_capitals.items():
    print(f"{country} -> {capital}")

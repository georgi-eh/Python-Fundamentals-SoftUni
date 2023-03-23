import re

input_string = input()
pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
match = re.findall(pattern, input_string)
travel_points = sum([len(points[1]) for points in match])
print(f"Destinations: {', '.join(destination[1] for destination in match)}")
print(f"Travel Points: {travel_points}")

destinations = ', '.join([destination[1] for destination in match])

command = input()

animals = {}
areas_with_hungry_animals = {}

while command != "EndDay":
    command_args = command.split(": ")
    if command_args[0] == "Add":
        animal, food_needed, area = command_args[1].split("-")
        food_needed = int(food_needed)
        if animal not in animals:
            animals[animal] = {"food_needed": food_needed,
                               "area": area}
        else:
            animals[animal]["food_needed"] += food_needed

    elif command_args[0] == "Feed":
        animal, food = command_args[1].split("-")
        food = int(food)
        if animal in animals:
            animals[animal]["food_needed"] -= food
            if animals[animal]["food_needed"] <= 0:
                print(f"{animal} was successfully fed")
                animals.pop(animal)
    command = input()

print("Animals:")
for animal in animals:
    print(f"{animal} -> {animals[animal]['food_needed']}g")

for val in animals.values():
    area = val["area"]
    if area not in areas_with_hungry_animals:
        areas_with_hungry_animals[area] = 0
    areas_with_hungry_animals[area] += 1

print(f"Areas with hungry animals:")
for area, count in areas_with_hungry_animals.items():
    print(f"{area}: {count}")

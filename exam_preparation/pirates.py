command = input()
cities = {}
while command != 'Sail':
    city = command.split('||')[0]
    population = int(command.split('||')[1])
    gold = int(command.split('||')[2])

    if city not in cities:
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += population
    cities[city]['gold'] += gold
    command = input()

command = input()
while command != 'End':
    if command.startswith('Plunder'):
        town = command.split('=>')[1]
        people_killed = int(command.split('=>')[2])
        gold_stolen = int(command.split('=>')[3])

        print(f'{town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.')
        cities[town]['population'] -= people_killed
        cities[town]['gold'] -= gold_stolen
        if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
            cities.pop(town)
            print(f'{town} has been wiped off the map!')

    elif command.startswith('Prosper'):
        town = command.split('=>')[1]
        gold_increase = int(command.split('=>')[2])

        if gold_increase < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities[town]["gold"] += gold_increase
            print(f'{gold_increase} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')
    command = input()

if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city in cities:
        print(f'{city} -> Population: {cities[city]["population"]} citizens, Gold: {cities[city]["gold"]} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')

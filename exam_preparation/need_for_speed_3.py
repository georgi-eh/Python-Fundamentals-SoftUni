num_of_cars = int(input())
cars = {}
for _ in range(num_of_cars):
    car, mileage, fuel = input().split('|')
    if car not in cars:
        cars[car] = {'mileage': 0,
                     'fuel': 0}
    cars[car]['mileage'] += int(mileage)
    cars[car]['fuel'] += int(fuel)

command = input()
while command != 'Stop':
    command_args = command.split(' : ')
    if command_args[0] == 'Drive':
        car = command_args[1]
        distance = int(command_args[2])
        fuel = int(command_args[3])

        if fuel > cars[car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

            if cars[car]['mileage'] >= 100000:
                print(f'Time to sell the {car}!')
                cars.pop(car)

    elif command_args[0] == 'Refuel':
        car = command_args[1]
        fuel = int(command_args[2])
        current_fuel = cars[car]['fuel']
        cars[car]['fuel'] += fuel
        if cars[car]['fuel'] > 75:
            cars[car]['fuel'] = 75
            fuel_refilled = 75 - current_fuel
            print(f'{car} refueled with {fuel_refilled} liters')
        else:
            print(f'{car} refueled with {fuel} liters')

    elif command_args[0] == 'Revert':
        car = command_args[1]
        kilometers = int(command_args[2])
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')
    command = input()

for car in cars.keys():
    mileage = cars[car]['mileage']
    fuel = cars[car]['fuel']
    print(f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')

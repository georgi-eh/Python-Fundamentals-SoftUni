water_tank_capacity = 255
liters_in_tank = 0
num_of_prompts = int(input())

for _ in range(num_of_prompts):
    liters = int(input())

    if liters_in_tank + liters > water_tank_capacity:
        print("Insufficient capacity!")
        continue
    elif liters_in_tank <= water_tank_capacity:
        liters_in_tank += liters

print(liters_in_tank)

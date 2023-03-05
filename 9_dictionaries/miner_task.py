command = input()
bag = {}
while command != "stop":
    quantity = int(input())
    resource = command
    if resource not in bag:
        bag[resource] = quantity
    else:
        bag[resource] += quantity

    command = input()

for key, value in bag.items():
    print(f"{key} -> {value}")

number_of_commands = int(input())
parking_lot = {}
for _ in range(number_of_commands):
    command = input().split()
    user = command[1]
    if command[0] == "register":
        license_plate = command[2]
        if user in parking_lot and license_plate in parking_lot[user]:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking_lot[user] = license_plate
            print(f"{user} registered {license_plate} successfully")
    else:
        if user not in parking_lot:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
for user in parking_lot:
    print(f"{user} => {parking_lot[user]}")

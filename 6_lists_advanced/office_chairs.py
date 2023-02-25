number_of_rooms = int(input())
free_chairs = 0
available_chairs = True

for room in range(1, number_of_rooms + 1):
    user_input = input().split()
    number_of_chairs = len(user_input[0])
    number_of_people = int(user_input[1])
    if number_of_people > number_of_chairs:
        chairs_needed = number_of_people - number_of_chairs
        print(f"{chairs_needed} more chairs needed in room {room}")
        available_chairs = False
    else:
        free_chairs += number_of_chairs - number_of_people
if available_chairs:
    print(f"Game On, {free_chairs} free chairs left")

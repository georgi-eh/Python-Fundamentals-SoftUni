total_energy = 100
total_coins = 100
factory_open = True

events = input().split("|")

for event in events:
    # type_of_event, event_value = event.split("-")
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])

    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50  # no need to check for energy > 100, because you enter else if energy is 29 or lower
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_open = False
            break

if factory_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

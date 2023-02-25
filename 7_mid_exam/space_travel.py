list_of_commands = input().split("||")
start_fuel = int(input())
start_ammunition = int(input())

for command in list_of_commands:
    if len(command.split()) == 1:
        print("You have reached Titan, all passengers are safe.")
    else:
        current_command = command.split()[0]
        command_number = int(command.split()[1])

        if current_command == "Travel":
            start_fuel -= command_number
            if start_fuel >= 0:
                print(f"The spaceship travelled {command_number} light-years.")
            else:
                print("Mission failed.")
                break
        if current_command == "Enemy":
            if start_ammunition >= command_number:
                start_ammunition -= command_number
                print(f"An enemy with {command_number} armour is defeated.")
            else:
                if command_number * 2 <= start_fuel:
                    start_fuel -= command_number * 2
                    print(f"An enemy with {command_number} armour is outmaneuvered.")
                else:
                    print("Mission failed.")
                    break
        if current_command == "Repair":
            start_fuel += command_number
            start_ammunition += command_number * 2
            print(f"Ammunitions added: {command_number * 2}.")
            print(f"Fuel added: {command_number}.")

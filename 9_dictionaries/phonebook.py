command = input().split("-")
phonebook = {}
while len(command) > 1:
    contact_name = command[0]
    contact_number = command[1]
    phonebook[contact_name] = contact_number
    command = input().split("-")

for _ in range(int(command[0])):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

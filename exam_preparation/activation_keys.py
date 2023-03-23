activation_key = input()
lst_activation_key = []
for char in activation_key:
    lst_activation_key.append(char)

command = input()

while command != "Generate":
    lst_of_commands = command.split('>>>')

    if lst_of_commands[0] == 'Contains':
        substring = lst_of_commands[1]
        if substring in ''.join(lst_activation_key):
            print(f"{''.join(lst_activation_key)} contains {substring}")
        else:
            print('Substring not found!')
    elif lst_of_commands[0] == "Flip":
        upper_or_lower = lst_of_commands[1]
        start_index = int(lst_of_commands[2])
        end_index = int(lst_of_commands[3])

        if upper_or_lower == 'Upper':
            for idx in range(start_index, end_index):
                lst_activation_key[idx] = lst_activation_key[idx].upper()
        elif upper_or_lower == 'Lower':
            for idx in range(start_index, end_index):
                lst_activation_key[idx] = lst_activation_key[idx].lower()
        print(''.join(lst_activation_key))
    elif lst_of_commands[0] == 'Slice':
        start_index = int(lst_of_commands[1])
        end_index = int(lst_of_commands[2])
        activation_key_left = lst_activation_key[0:start_index]
        activation_key_right = lst_activation_key[end_index::]
        lst_activation_key = activation_key_left + activation_key_right
        print(''.join(lst_activation_key))
    command = input()
print(f"Your activation key is: {''.join(lst_activation_key)}")

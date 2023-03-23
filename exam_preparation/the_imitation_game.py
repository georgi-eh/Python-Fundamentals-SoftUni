encrypted_message = [char for char in input()]
command = input()

while command != "Decode":
    lst_of_commands = command.split('|')
    current_command = lst_of_commands[0]

    if current_command == 'Move':
        num_of_letters = int(lst_of_commands[1])
        right_part = encrypted_message[0:num_of_letters]
        left_part = encrypted_message[num_of_letters::]
        encrypted_message = left_part + right_part
    elif current_command == 'Insert':
        idx = int(lst_of_commands[1])
        value = lst_of_commands[2]
        encrypted_message.insert(idx, value)
    elif current_command == 'ChangeAll':
        substring = lst_of_commands[1]
        replacement = lst_of_commands[2]
        for idx, char in enumerate(encrypted_message):
            if char == substring:
                encrypted_message[idx] = replacement
    command = input()
print(f'The decrypted message is: {"".join(encrypted_message)}')

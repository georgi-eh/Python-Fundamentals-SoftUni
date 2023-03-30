concealed_message = input()

command = input()

while command != "Reveal":
    command_args = command.split(":|:")
    current_command = command_args[0]

    if current_command == "InsertSpace":
        idx = int(command_args[1])
        concealed_message = concealed_message[:idx] + " " + concealed_message[idx:]
        print(concealed_message)
    elif current_command == "Reverse":
        substring = command_args[1]
        if substring in concealed_message:
            start_idx = concealed_message.index(substring[0])
            end_idx = concealed_message.index(substring[len(substring) - 1]) # PROBLEM: could be another such symbol on the original string
            reversed_substring = substring[::-1]
            concealed_message = concealed_message[:start_idx] + concealed_message[end_idx + 1:] + reversed_substring
            print(concealed_message)
        else:
            print("error")
    elif current_command == "ChangeAll":
        substring_to_replace = command_args[1]
        replacement = command_args[2]
        concealed_message = concealed_message.replace(substring_to_replace, replacement)
        print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")

def is_index_valid(idx, iterable):
    return idx in range(0, len(iterable))


text = input()
command = input()

while command != "Finish":
    command_args = command.split()
    if command_args[0] == "Replace":
        current_char, new_char = command_args[1:]
        text = text.replace(current_char, new_char)
        print(text)
    elif command_args[0] == "Cut":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if is_index_valid(start_index, text) and is_index_valid(end_index, text):
            text = text[:start_index] + text[end_index + 1:]
            print(text)
        else:
            print("Invalid indices!")
    elif command_args[0] == "Make":
        upper_lower = command_args[1]
        if upper_lower == "Upper":
            text = text.upper()
        elif upper_lower == "Lower":
            text = text.lower()
        print(text)
    elif command_args[0] == "Check":
        substring = command_args[1]
        if substring in text:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif command_args[0] == "Sum":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if is_index_valid(start_index, text) and is_index_valid(end_index, text):
            substring = text[start_index: end_index + 1]
            total_sum = 0
            for char in substring:
                total_sum += ord(char)
            print(total_sum)
        else:
            print("Invalid indices!")

    command = input()

while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    new_command = ""
    for char in range(len(command)):
        new_command += command[char] * 2
    else:
        print(new_command)


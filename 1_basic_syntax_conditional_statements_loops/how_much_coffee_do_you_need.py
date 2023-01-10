coffee = 0
list_of_commands = ["coding", "dog", "cat", "movie",
                    "CODING", "DOG", "CAT", "MOVIE"]

while True:
    command = input()
    if command == "END":
        if coffee > 5:
            print("You need extra sleep")
            break
        else:
            print(coffee)
            break
    if command not in list_of_commands:
        continue
    else:
        if command.isupper():
            coffee += 2
        else:
            coffee += 1

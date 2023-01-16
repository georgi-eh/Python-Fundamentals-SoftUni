gifts = input().split()
command = input()

while command != "No Money":
    list_of_command = command.split()
    if list_of_command[0] == "OutOfStock":
            for _ in gifts:
                if list_of_command[1] in gifts:
                    index_to_replace = gifts.index(list_of_command[1])
                    gifts[index_to_replace] = None
    elif list_of_command[0] == "Required":
         if int(list_of_command[2]) in range(len(gifts)):
             gifts[int(list_of_command[2])] = list_of_command[1]
    elif list_of_command[0] == "JustInCase":
        gifts[-1] = list_of_command[1]

    command = input()

filtered_list = list(filter(None, gifts))

final_list = " ".join(filtered_list)
print(final_list)

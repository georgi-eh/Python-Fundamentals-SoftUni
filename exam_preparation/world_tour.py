def index_is_valid(index, iterable):
    return index in range(0, len(iterable) - 1)


itinerary = [char for char in input()]

command = input()

while command != 'Travel':
    command_parts = command.split(':')
    if command_parts[0].startswith('Add'):
        index = int(command_parts[1])
        string = command_parts[2]
        if index_is_valid(index, itinerary):
            new_place = [char for char in string]
            left_part = itinerary[0: index]
            right_part = itinerary[index::]
            itinerary = left_part + new_place + right_part

    elif command_parts[0].startswith('Remove'):
        start_index, end_index = [int(x) for x in command_parts[1::]]
        if index_is_valid(start_index, itinerary) and index_is_valid(end_index, itinerary):
            left_part = itinerary[0: start_index]
            right_part = itinerary[end_index + 1::]
            itinerary = left_part + right_part
    elif command_parts[0].startswith('Switch'):
        old_string, new_string = command_parts[1::]
        if old_string in ''.join(itinerary):
            new_itinerary = ''.join(itinerary).replace(old_string, new_string)
            itinerary = new_itinerary

    print(''.join(itinerary))
    command = input()
print(f'Ready for world tour! Planned stops: {"".join(itinerary)}')

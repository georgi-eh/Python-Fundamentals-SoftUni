def index_is_valid(index, iterable):
    return index in range(0, len(iterable) - 1)


itinerary = input()

command = input()

while command != 'Travel':
    command_parts = command.split(':')

    if command_parts[0].startswith('Add'):
        index = int(command_parts[1])
        new_stop = command_parts[2]
        if index_is_valid(index, itinerary):
            left_part = itinerary[:index]
            right_part = itinerary[index:]
            itinerary = left_part + new_stop + right_part
    elif command_parts[0].startswith('Remove'):
        start_index, end_index = [int(x) for x in command_parts[1:]]
        if index_is_valid(start_index, itinerary) and index_is_valid(end_index, itinerary):
            left_part = itinerary[:start_index]
            right_part = itinerary[end_index + 1:]
            itinerary = left_part + right_part
    elif command_parts[0].startswith('Switch'):
        old_string, new_string = command_parts[1:]
        itinerary = itinerary.replace(old_string, new_string)

    command = input()
    print(itinerary)
print(f'Ready for world tour! Planned stops: {itinerary}')

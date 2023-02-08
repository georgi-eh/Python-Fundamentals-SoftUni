def merge(list_data, start, end):
    if end >= len(list_data):
        end = len(list_data) - 1

    if start < 0:
        start = 0

    for merge_index in range(start + 1, end + 1):
        list_data[start] += list_data[merge_index]
    for remove_index in range(end, start, -1):
        list_data.remove(list_data[remove_index])

    return list_data


def divide(list_data, index, number_of_partitions):
    string_to_divide = list_data[index]
    string_divided = list_data[index]
    if number_of_partitions > 0:
        length_of_each_partition = len(list_data[index]) // number_of_partitions
        remainder_to_add_to_the_last_partition = len(list_data[index]) % number_of_partitions
        for index_of_partition in range(index, index + number_of_partitions):
            partition_to_insert = string_divided[0:length_of_each_partition]
            
            list_data.insert(index_of_partition, partition_to_insert)

            string_divided = string_divided[length_of_each_partition::]

        if remainder_to_add_to_the_last_partition > 0:
            list_data[index + number_of_partitions - 1] = list_data[number_of_partitions - 1] + string_divided

        list_data.remove(string_to_divide)

    return list_data


input_data = input().split()
command = input().split()
action = command[0]
while action != "3:1":
    start_index = int(command[1])
    index = int(command[1])
    end_index = int(command[2])
    partitions = int(command[2])

    if action == "merge":
        merge(input_data, start_index, end_index)
    elif action == "divide":
        divide(input_data, index, partitions)

    command = input().split()
    action = command[0]

print(*input_data)
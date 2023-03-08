first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    for idx in range(len(second_string)):
        total_sum += ord(first_string[idx]) * ord(second_string[idx])
    for idx in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[idx])

elif len(second_string) > len(first_string):
    for idx in range(len(first_string)):
        total_sum += ord(first_string[idx]) * ord(second_string[idx])
    for idx in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[idx])
else:
    for idx in range(len(first_string)):
        total_sum += ord(first_string[idx]) * ord(second_string[idx])
print(total_sum)

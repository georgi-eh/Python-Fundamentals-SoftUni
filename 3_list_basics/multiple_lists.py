factor = int(input())
count = int(input())

list_of_numbers = []

for multiplier in range(1, count + 1):
    current_num = factor * multiplier
    list_of_numbers.append(current_num)

print(list_of_numbers)

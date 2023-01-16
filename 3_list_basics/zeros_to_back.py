list_of_nums = input().split(", ")
new_list = []
list_of_integers = []
zeroes_counter = 0

for integer in (list_of_nums):
    if integer != "0":
        new_list.append(integer)
    else:
        zeroes_counter += 1

for _ in range(zeroes_counter):
    new_list.append("0")

for num in new_list:
    list_of_integers.append(int(num))

print(list_of_integers)


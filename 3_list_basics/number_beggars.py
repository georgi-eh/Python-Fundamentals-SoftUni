money_list = input().split(", ")
count_of_beggars = int(input())

final_sums = []
money_list_as_int = []
start_index = 0

for element in money_list:
    money_list_as_int.append(int(element))

while start_index < count_of_beggars:
    sum_current_beggar = 0
    for current_index in range(start_index, len(money_list_as_int), count_of_beggars):
        sum_current_beggar += money_list_as_int[current_index]
    final_sums.append(sum_current_beggar)
    start_index += 1

print(final_sums)

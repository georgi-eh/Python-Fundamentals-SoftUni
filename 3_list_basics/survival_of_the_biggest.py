
list_numbers = input().split()
big_numbers = []
string_list = []

for number in list_numbers:
    big_numbers.append(int(number))

remover = int(input())

for removing in range(remover):
    big_numbers.remove(min(big_numbers))

for integer in big_numbers:
    string_list.append(str(integer))

string_of_nums = ", ". join(string_list)

print(string_of_nums)

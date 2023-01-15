# list_of_strings = input().split()
# count_of_numbers_to_remove = int(input())
# list_of_integers = []
# string_list = []
#
# for num in list_of_strings:
#     list_of_integers.append(int(num))
#
# list_of_integers.sort(reverse=True)
#
# for _ in range(count_of_numbers_to_remove):
#     list_of_integers.pop()
# for integer in list_of_integers:
#     string_list.append(str(integer))
#
# string_of_integers = ", ".join(string_list)
#
# print(string_of_integers)

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
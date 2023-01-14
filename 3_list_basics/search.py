number = int(input())
word = input()
list_of_strings = list()
new_list = list()

for _ in range(number):
    command = input()
    list_of_strings.append(command)

for idx in range(len(list_of_strings)):
    if list_of_strings[idx].find(word) >= 0:
        new_list.append(list_of_strings[idx])

print(list_of_strings)
print(new_list)
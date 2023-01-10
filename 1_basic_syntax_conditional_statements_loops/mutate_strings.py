first_str = input()
second_str = input()
str_list = []
for i in range(len(first_str)):
    if first_str[i] != second_str[i]:
        str_list = list(first_str)
        str_list[i] = second_str[i]
        first_str = ''.join(str_list)
        print(first_str)



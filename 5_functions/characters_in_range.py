def chars_in_range(char_one, char_two):
    start_num = ord(char_one)
    stop_num = ord(char_two)
    list_of_chars = []
    for idx in range(start_num + 1, stop_num):
        list_of_chars.append(chr(idx))
    string_of_chars = " ".join(list_of_chars)
    return string_of_chars

char_one = input()
char_two = input()

result = chars_in_range(char_one, char_two)

print(result)

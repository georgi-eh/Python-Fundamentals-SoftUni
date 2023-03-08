input_string = input()
new_string = ""
for idx in range(len(input_string)):
    if idx == 0:
        new_string += input_string[idx]
    elif input_string[idx] != input_string[idx - 1]:
        new_string += input_string[idx]
print(new_string)

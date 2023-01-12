key = int(input())
num_of_lines = int(input())

for _ in range(num_of_lines):
    letter = input()
    new_letter = chr(ord(letter) + key)
    print(new_letter, end="")

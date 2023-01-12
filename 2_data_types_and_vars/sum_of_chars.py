num_of_lines = int(input())
total = 0

for _ in range(num_of_lines):
    char = input()
    total += ord(char)

print(f"The sum equals: {total}")
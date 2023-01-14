num_of_lines = int(input())
numbers = []
filtered_nums = []

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

for _ in range(num_of_lines):
    num = int(input())
    numbers.append(num)

command = input()

for number in numbers:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_POSITIVE and number >= 0) or
        (command == COMMAND_NEGATIVE and number < 0)
    )

    if filtered_passes:
        filtered_nums.append((number))

print(filtered_nums)

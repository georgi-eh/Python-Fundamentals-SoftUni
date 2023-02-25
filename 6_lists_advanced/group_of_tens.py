list_of_nums = list(map(int, input().split(", ")))
group_number = 10

filtered_nums = []

if max(list_of_nums) % 10 == 0:
    number_of_iterations = max(list_of_nums) // 10
else:
    number_of_iterations = (max(list_of_nums) // 10) + 1


def range_check(number):
    if group_number >= number > group_number - 10:
        return True
    else:
        return False


for _ in range(number_of_iterations):
    filtered_nums = list(filter(range_check, list_of_nums))
    print(f"Group of {group_number}'s: {filtered_nums}")
    filtered_nums.clear()
    group_number += 10

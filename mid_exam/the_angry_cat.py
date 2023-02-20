items = list(map(int, input().split(", ")))
entry_point = int(input())
cheap_or_expensive = input()
left_sum = 0
right_sum = 0
left_list = items[:entry_point]
right_list = items[entry_point + 1:]
sum_to_compare = items[entry_point]
if cheap_or_expensive == "cheap":
    for item in left_list:
        if item < sum_to_compare:
            left_sum += item
    for item in right_list:
        if item < sum_to_compare:
            right_sum += item
else:
    for item in left_list:
        if item >= sum_to_compare:
            left_sum += item
    for item in right_list:
        if item >= sum_to_compare:
            right_sum += item

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")

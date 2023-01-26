def min_max_sum(list_of_nums):
    min_num = min(list_of_nums)
    max_num = max(list_of_nums)
    total_sum = sum(list_of_nums)
    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {total_sum}")

list_of_nums = list(map(int, input().split()))

min_max_sum(list_of_nums)

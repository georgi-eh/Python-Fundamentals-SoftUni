def rounder(list_of_nums):
    rounded_nums = []
    for num in list_of_nums:
        rounded_nums.append(round(float(num)))
    return rounded_nums

list_of_nums = input().split()
rounded_nums = rounder(list_of_nums)

print(rounded_nums)

numbers_string = input()
inverted_nums = []

# create a list from the string
list_of_nums = numbers_string.split(" ")

for num in range(len(list_of_nums)):
    inverted_num = int(list_of_nums[num]) * - 1
    inverted_nums.append(inverted_num)

print(inverted_nums)
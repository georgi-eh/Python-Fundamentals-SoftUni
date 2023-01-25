list_of_nums = input().split()
list_of_abs_vals = []

for num in list_of_nums:
    list_of_abs_vals.append(abs(float(num)))

print(list_of_abs_vals)
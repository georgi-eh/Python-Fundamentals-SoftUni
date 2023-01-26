def return_smallest_num(int_one, int_two, int_three):
    list_of_nums = [int_one, int_two, int_three]
    return min(list_of_nums)

int_one = int(input())
int_two = int(input())
int_three = int(input())

result = return_smallest_num(int_one, int_two, int_three)
print(result)

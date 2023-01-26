def check_even(number):
    if int(number) % 2 == 0:
        return True
    return False

list_of_nums = input().split()
list_of_even_nums = map(int,list(filter(check_even, list_of_nums)))
print(list(list_of_even_nums))









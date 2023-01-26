def sum_numbers(number_one, number_two):
    return number_one + number_two

def subtract_nums(number_one, number_two):
    return number_one - number_two

def add_and_subtract(number_one, number_two, number_three):
    sum_result = sum_numbers(number_one, number_two)
    subtract_result = subtract_nums(sum_result, number_three)
    return subtract_result

number_one = int(input())
number_two = int(input())
number_three = int(input())

result = add_and_subtract(number_one, number_two, number_three)
print(result)

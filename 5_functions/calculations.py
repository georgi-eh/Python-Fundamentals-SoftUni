def calculator(operator, first_num, second_num):
    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return first_num / second_num
    elif operator == "add":
        return first_num + second_num
    elif operator == "subtract":
        return first_num - second_num


input_operator = input().lower()
first_num = int(input())
second_num = int(input())

result = int(calculator(input_operator, first_num, second_num))
print(result)


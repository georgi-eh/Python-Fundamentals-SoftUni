def odd_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for digit in num:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

num = input()
odd_even_sum(num)

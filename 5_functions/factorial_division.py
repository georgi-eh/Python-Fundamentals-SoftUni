from math import factorial
def factorial_divisor(number_one, number_two):
    factorial_one = factorial(number_one)
    factorial_two = factorial(number_two)
    division_result = factorial_one / factorial_two
    print(f"{division_result:.2f}")

number_one = int(input())
number_two = int(input())

factorial_divisor(number_one, number_two)

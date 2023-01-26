def check_palindrome(list_of_nums):
    for num in list_of_nums:
        potential_palindrome = num[::-1]
        if num == potential_palindrome:
            print("True")
        else:
            print("False")

list_of_nums = input().split(", ")

check_palindrome(list_of_nums)

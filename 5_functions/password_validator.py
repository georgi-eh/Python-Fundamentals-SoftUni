def password_validator(password):
    digits = "0123456789"
    special_chars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    digit_counter = 0
    password_is_valid = True
    #   should be 6 - 10 (inclusive) characters long
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    #   should consist only of letters and digits
    #   should have at least 2 digits
    for char in password:
        if char in special_chars:
            print("Password must consist only of letters and digits")
            password_is_valid = False
            break
        if char in digits:
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False

    if password_is_valid:
        print("Password is valid")

user_password = input()
password_validator(user_password)

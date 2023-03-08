# def length_is_valid(name):
#     if 3 <= len(name) <= 16:
#         return True
#     return False
#
#
# def character_are_valid(name):
#     for character in name:
#         if not (character.isalnum() or character == "_" or character == "-"):
#             return False
#         return True
#
#
# def no_redundant_chars(name):
#     if " " in name:
#         return False
#     return True
#
#
# def username_validation(name):
#     if length_is_valid(name) and character_are_valid(name) and no_redundant_chars(name):
#         return True
#     return False
#
#
# usernames = input().split(", ")
# for username in usernames:
#     if username_validation(username):
#         print(username)

usernames = input().split(", ")
valid_usernames = []
is_valid = False
for username in usernames:
    if 3 <= len(username) <= 16:
        pass_check = ""
        for symbol in username:
            if symbol.isdigit() or symbol.isalpha() or chr(45) == symbol or chr(95) == symbol:
                pass_check += symbol
            if pass_check == username:
                print(f"{username}")

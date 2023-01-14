# # TODO: fix it :)
#
# num_of_lines = int(input())
# counter = 0
# list_of_chars = []
# balanced = False
# idx = 0
#
# for _ in range(num_of_lines):
#     char = input()
#     list_of_chars.append(char)
#
# while idx <= len(list_of_chars):
#     if list_of_chars[idx] == "(":
#         for inner_idx_a in range(idx + 1, len(list_of_chars)):
#             if list_of_chars[inner_idx_a] != ")":
#                 balanced = False
#                 continue
#             else:
#                 balanced = True
#                 idx = inner_idx_a + 1
#                 break
#     elif list_of_chars[idx] == ")":
#         for inner_idx_b in range(idx + 1, len(list_of_chars)):
#             if list_of_chars[inner_idx_b] != "(":
#                 balanced = False
#                 continue
#             else:
#                 balanced = True
#                 idx = inner_idx_b + 1
#                 break
#     else:
#         idx += 1
#         continue
#     if idx >= len(list_of_chars):
#         break
#
# if balanced:
#     print("BALANCED")
# else:
#     print("UNBALANCED")


num_of_lines = int(input())
list_of_chars = []
balanced = False
idx = 0

for _ in range(num_of_lines):
    char = input()
    if char == "(":
        if list_of_chars[idx] == char:
            balanced = False
            break
        elif char == ")":
            balanced = True
            continue
        list_of_chars.append(char)
        idx += 1
        continue

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")



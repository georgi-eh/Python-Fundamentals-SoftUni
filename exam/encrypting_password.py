import re

num_of_inputs = int(input())
pattern = r"([\[\]{}\\$&+,:;=?@#|'<>.^*()%!\-\w]+)>(\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1$"

for _ in range(num_of_inputs):
    current_password = input()
    match = re.findall(pattern, current_password)

    if match:
        print(f'Password: {match[0][1].replace("|", "")}')
    else:
        print(f"Try another password!")

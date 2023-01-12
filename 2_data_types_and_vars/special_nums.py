iterations = int(input())
total = 0
for num in range(1, iterations + 1):
    for digit in str(num):
        total += int(digit)

    if total in [5, 7, 11]:
        print(f"{num} -> True")
        total = 0
    else:
        print(f"{num} -> False")
        total = 0



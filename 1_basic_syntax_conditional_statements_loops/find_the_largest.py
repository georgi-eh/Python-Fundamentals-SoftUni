num = input()
final_num = ""

largest = list(num)
largest.sort(reverse=True)

for digit in  largest:
    final_num += digit

print(int(final_num))
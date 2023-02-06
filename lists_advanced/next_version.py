version = input().split(".")
version_list = [int(number) for number in version]
version_list[-1] += 1
for index in range(len(version_list) - 1, -1, -1):
    if version_list[index] > 9:
        version_list[index] = 0
        if index - 1 >= 0:
            version_list[index - 1] += 1

print(".".join(str(number) for number in version_list))

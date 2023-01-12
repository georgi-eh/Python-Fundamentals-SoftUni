string = input().lower()
counter = 0

counter += string.count("sun") + string.count("sand") + string.count("water") + string.count("fish")

print(counter)
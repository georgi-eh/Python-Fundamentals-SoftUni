text = input().split()
count_of_chars = {}
for word in text:
    for letter in word:
        if letter not in count_of_chars:
            count_of_chars[letter] = 1
        else:
            count_of_chars[letter] += 1

for key, value in count_of_chars.items():
    print(f"{key} -> {value}")

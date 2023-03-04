data = input().lower().split()
dict_of_words = {}
odd_occurences = []
for word in data:
    if word in dict_of_words:
        dict_of_words[word] += 1
    else:
        dict_of_words[word] = 1

for key, value in dict_of_words.items():
    if value % 2 != 0:
        odd_occurences.append(key)

print(" ".join(odd_occurences))

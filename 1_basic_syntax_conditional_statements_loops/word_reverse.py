word = input()

word_reversed = ""
for char in range(len(word) - 1, -1, -1):
    word_reversed += word[char]

print(word_reversed)
import re

sentence = input()
word = input()
pattern = rf"{word}\b"

words_found = re.findall(pattern, sentence, re.IGNORECASE)
print(len(words_found))

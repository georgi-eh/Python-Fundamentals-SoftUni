list_of_words = input().split()
list_of_digits = [str(x) for x in range(10)]
final_string = ""
for word in list_of_words:
    digits_in_word = [digit for digit in word if digit in list_of_digits]
    characters_in_word = [chr for chr in word if chr not in list_of_digits]
    ascii_number = int("".join(digits_in_word))
    characters_in_word[0], characters_in_word[-1] = characters_in_word[-1], characters_in_word[0]
    characters_in_word = "".join(characters_in_word)
    current_word = chr(ascii_number) + characters_in_word
    print(current_word, end=" ")

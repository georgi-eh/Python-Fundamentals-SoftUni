characters = input().split(", ")
dict_of_ascii_values = {character: ord(character) for character in characters}
print(dict_of_ascii_values)

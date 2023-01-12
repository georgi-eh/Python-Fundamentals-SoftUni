string = input()    # string

# remove whitespaces
stripped_string = string.replace(" ", "")

# turn string to list
string_list = stripped_string.split(",")

if string_list.index("wolf") == len(string_list) - 1:
    print("Please go away and stop eating my sheep")
else:
    index_sheep = len(string_list) - 1 - string_list.index("wolf")
    print(f"Oi! Sheep number {index_sheep}! You are about to be eaten by a wolf!")
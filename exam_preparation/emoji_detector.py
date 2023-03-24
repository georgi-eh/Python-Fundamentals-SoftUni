import re


def coolness(emoji):
    coolness = 0
    for char in emoji:
        coolness += ord(char)
    return coolness


def prod(lst):
    # Multiply elements one by one
    result = 1
    for x in lst:
        result = result * x
    return result


emojis_count = 0
emojis_to_print = []

text = input()
emoji_pattern_with_symbols = r'(::)([A-Z]{1}[a-z]{2,})(::)|(\*\*)([A-Z]{1}[a-z]{2,})(\*\*)'
emojis_with_symbols = re.finditer(emoji_pattern_with_symbols, text)
digit_matches = [int(x) for x in re.findall(r'\d', text)]
coolness_threshold = prod(digit_matches)

print(f'Cool threshold: {coolness_threshold}')

for emoji_group in emojis_with_symbols:

    emoji = emoji_group.group()
    pattern = r'\w+'
    clear_emoji = re.findall(pattern, emoji)[0]  # returns a list
    emojis_count += 1
    if coolness(clear_emoji) >= coolness_threshold:
        emojis_to_print.append(emoji)
print(f'{emojis_count} emojis found in the text. The cool ones are:')

print(*emojis_to_print, sep='\n')

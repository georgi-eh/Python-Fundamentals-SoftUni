text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

lst = [ch for ch in text if ch.lower() not in vowels]
print("".join(lst))

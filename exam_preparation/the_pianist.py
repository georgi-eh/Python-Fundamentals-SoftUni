number_of_pieces = int(input())
song_list = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    song_list[piece] = [composer, key]

command = input()
while command != 'Stop':
    command_parts = command.split('|')
    if command_parts[0] == 'Add':
        piece, composer, key = command_parts[1::]
        if piece in song_list:
            print(f'{piece} is already in the collection!')
        else:
            song_list[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
    elif command_parts[0] == 'Remove':
        piece = command_parts[1]
        if piece in song_list:
            song_list.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif command_parts[0] == 'ChangeKey':
        piece, new_key = command_parts[1::]
        if piece in song_list:
            song_list[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    command = input()
for piece, composer_key in song_list.items():
    print(f'{piece} -> Composer: {composer_key[0]}, Key: {composer_key[1]}')

def avg(lst):
    if len(lst) > 0:
        return sum(lst) / len(lst)
    return 0


num_of_plants = int(input())
plants = {}
for _ in range(num_of_plants):
    plant, rarity = input().split('<->')
    if plant not in plants:
        plants[plant] = {'rarity': "",
                         'rating': []}
    plants[plant]['rarity'] = rarity

command = input()

while command != 'Exhibition':
    current_command = command.split(': ')[0]
    args = command.split(': ')[1]
    plant = args.split(' - ')[0]
    if plant not in plants:
        print('error')
    else:
        if current_command == 'Rate':
            rating = int(args.split(' - ')[1])
            plants[plant]['rating'].append(rating)
        elif current_command == 'Update':
            new_rarity = args.split(' - ')[1]
            plants[plant]['rarity'] = new_rarity
        elif current_command == 'Reset':
            plants[plant]['rating'].clear()

    command = input()

print('Plants for the exhibition:')
for plant in plants.keys():
    rarity = plants[plant]['rarity']
    avg_rating = avg(plants[plant]['rating'])
    print(f'- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}')

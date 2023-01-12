lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = 0
broken_swords = 0
broken_shields = 0
broken_armor = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        broken_helmets += 1
    if fight % 3 == 0:
        broken_swords += 1
        if fight % 2 == 0:
            broken_shields += 1
            if broken_shields % 2 == 0:
                broken_armor += 1

total_expense = broken_helmets * helmet_price + \
                broken_swords * sword_price + \
                broken_shields * shield_price + \
                broken_armor * armor_price

print(f"Gladiator expenses: {total_expense:.2f} aureus")

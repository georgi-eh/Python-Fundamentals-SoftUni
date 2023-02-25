from math import ceil

budget = float(input())
num_of_students = int(input())
flour_price = float(input())  # per package
egg_price = float(input())  # per one egg
apron_price = float(input())  # per single apron
money_spent = float()
eggs_needed = 0
aprons_needed = 0
flour_needed = 0

for student in range(1, num_of_students + 1):
    eggs_needed += 10
    aprons_needed += 1
    flour_needed += 1
    if student % 5 == 0:
        flour_needed -= 1

money_spent = (eggs_needed * egg_price) + (ceil(aprons_needed * 1.2) * apron_price) + flour_needed * flour_price
money_needed = budget - money_spent
if money_needed >= 0:
    print(f"Items purchased for {money_spent:.2f}$.")
else:
    print(f"{abs(money_needed):.2f}$ more needed.")

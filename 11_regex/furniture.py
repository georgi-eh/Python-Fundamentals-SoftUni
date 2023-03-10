import re

pattern = r">>(\b\w+)<<(\d+.?\d+)!(\d+)"
money_spent = 0
items_bought = []

command = input()

while command != "Purchase":
    obj = re.search(pattern, command)
    if obj:
        items_bought.append(obj.group(1))
        money_spent += float(obj.group(2)) * float(obj.group(3))

    command = input()
print("Bought furniture:")
for furniture in items_bought:
    print(furniture)
print(f"Total money spend: {money_spent:.2f}")

key_items = {"shards": 0, "fragments": 0, "motes": 0}
garbage = {}
number = 0
is_lower = True
while is_lower:
    line_items = input().split(" ")
    for i in range(0, len(line_items), 2):
        number = int(line_items[i])
        item = line_items[i + 1].lower()
        if item in key_items.keys():
            key_items[item] += number
            if key_items[item] >= 250:
                legendary_item = " "
                if item == "shards":
                    legendary_item = "Shadowmourne"
                elif item == "fragments":
                    legendary_item = "Valanyr"
                elif item == "motes":
                    legendary_item = "Dragonwrath"
                print(f"{legendary_item} obtained!")
                key_items[item] -= 250
                is_lower = False
                break

        elif item in garbage.keys():
            garbage[item] += number
        else:
            garbage[item] = number

for material, quantity in key_items.items():
    print(f"{material}: {quantity}")
for material, quantity in garbage.items():
    print(f"{material}: {quantity}")

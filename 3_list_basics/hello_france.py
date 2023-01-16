# TODO: ONLY 70/100

ticket_price = 150
items = input().split("|")
budget = float(input())
bought_items = []
new_prices = []
format_prices = []
revenue = 0
profit = 0

CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE = 20.50

for item in items:
    item_type = item.split("->")[0]
    item_price = float(item.split("->")[1])

    check_passes = ((item_type == "Clothes" and item_price < CLOTHES_MAX_PRICE and item_price <= budget) or
                    (item_type == "Shoes" and item_price < SHOES_MAX_PRICE and item_price <= budget) or
                    (item_type == "Accessories" and item_price < ACCESSORIES_MAX_PRICE and item_price <= budget))

    if check_passes:
        budget -= item_price
        new_price =  1.4 * item_price
        revenue += new_price
        new_prices.append(new_price)
        bought_items.append(item_type)
        profit += 0.4 * item_price

for price in new_prices:
    format_price = format(price, ".2f")
    format_prices.append(format_price)


print(*format_prices)
print(f"Profit: {profit:.2f}")

if budget + revenue >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")


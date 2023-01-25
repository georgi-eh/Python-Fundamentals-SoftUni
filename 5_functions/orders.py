COFFEE_PRICE = 1.5
WATER_PRICE = 1
COKE_PRICE = 1.4
SNACKS_PRICE = 2

def order_price(product, quantity):
    if product == "coffee":
        return quantity * COFFEE_PRICE
    elif product == "water":
        return quantity * WATER_PRICE
    elif product == "coke":
        return quantity * COKE_PRICE
    elif product == "snacks":
        return quantity * SNACKS_PRICE

input_product = input().lower()
input_quantity = int(input())

total_price = order_price(input_product, input_quantity)
print(f"{total_price:.2f}")

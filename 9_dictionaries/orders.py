command = input().split()
product_catalogue = {}

while command != ['buy']:
    product_name = command[0]
    list_of_price_and_quantity = command[1:]
    if product_name not in product_catalogue:
        product_catalogue[product_name] = list(map(float, list_of_price_and_quantity))
    else:
        product_catalogue[product_name][0] = list_of_price_and_quantity[0]
        product_catalogue[product_name][1] += float(list_of_price_and_quantity[1])
    command = input().split()

for product, price_quantity in product_catalogue.items():
    total_amount = float(price_quantity[0]) * float(price_quantity[1])
    print(f"{product} -> {total_amount:.2f}")

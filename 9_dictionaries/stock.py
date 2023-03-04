data = input().split()
products = {}
for idx in range(0, len(data), 2):
    key = data[idx]
    value = int(data[idx + 1])
    products[key] = value

searched_items = input().split()

for product in searched_items:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

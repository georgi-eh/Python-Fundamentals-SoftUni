data = input().split()
products = {}
for idx in range(0, len(data), 2):
    key = data[idx]
    value = int(data[idx + 1])
    products[key] = value
print(products)

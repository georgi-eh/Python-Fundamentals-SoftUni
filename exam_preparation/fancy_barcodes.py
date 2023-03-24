import re

pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

n = int(input())

for _ in range(n):
    data = input()
    if re.match(pattern, data):
        digits = re.findall(r'\d+', data)
        if digits:
            product_group = ''.join(digits)
        else:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')

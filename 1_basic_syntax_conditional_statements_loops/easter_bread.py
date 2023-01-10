budget = float(input())
price_flour = float(input()) # price per 1 kg
price_eggs = price_flour * 0.75 # per 1 pack
price_milk = price_flour * 1.25 # per 1 l
price_per_loaf = price_flour + price_eggs + (price_milk * 1/4) # money needed to make 1 loaf
eggs = 0
num_of_loaves = 0

while budget >= price_per_loaf:
    budget -= price_per_loaf
    num_of_loaves += 1
    eggs += 3

    if num_of_loaves % 3 == 0:
        eggs -= num_of_loaves - 2

print(f"You made {num_of_loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")

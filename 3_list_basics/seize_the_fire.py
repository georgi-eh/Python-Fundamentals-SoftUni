total_effort = 0
total_fire = 0
cells_put_out = []

fire_list = input().split("#")
amount_of_water = int(input())

for fire in fire_list:
    fire_type = fire.split(" = ")[0]
    water_needed = int(fire.split(" = ")[1])

    check_passes = ((fire_type == "High" and water_needed in range(81, 126) and amount_of_water >= water_needed) or
                    (fire_type == "Medium" and water_needed in range(51, 81) and amount_of_water >= water_needed) or
                    (fire_type == "Low" and water_needed in range(1, 51) and amount_of_water >= water_needed))
    if check_passes:
        amount_of_water -= water_needed
        total_effort += 0.25 * water_needed
        total_fire += water_needed
        cells_put_out.append(water_needed)

print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

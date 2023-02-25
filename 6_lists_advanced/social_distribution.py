population = list(map(int, input().split(", ")))
min_wealth = int(input())
final_list = []
richest_person = max(population)
current_richest_person = richest_person
social_distribution = True
for person in population:
    person_wealth = person
    if person_wealth < min_wealth:
        wealth_needed = min_wealth - person_wealth
        if current_richest_person - wealth_needed > min_wealth:
            person_wealth += wealth_needed
            current_richest_person -= wealth_needed
    if person_wealth != richest_person:
        final_list.append(person_wealth)
    else:
        final_list.append(current_richest_person)
print(final_list)
for current_person in final_list:
    if current_person < min_wealth:
        social_distribution = False
if social_distribution:
    print(final_list)
else:
    print("No equal distribution possible")

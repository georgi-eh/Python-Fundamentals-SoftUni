num_people = int(input())
elevator_capacity = int(input())

courses = num_people // elevator_capacity

if num_people - courses * elevator_capacity > 0 and (num_people % elevator_capacity) // elevator_capacity == 0:
    courses += 1

print(courses)
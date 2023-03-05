next_rows_number = int(input())
grades = {}
average_of_grades = {}

for i in range(next_rows_number):
    name = input()
    grade = float(input())
    if name not in grades.keys():
        grades[name] = []
    grades[name].append(grade)

for name, grade in grades.items():
    average_grade = sum(grade) / len(grade)
    average_of_grades[name] = average_grade

sorted_average_grades = dict(filter(lambda x: x[1] >= 4.5, average_of_grades.items()))

for name, av_grade in sorted_average_grades.items():
    print(f"{name} -> {av_grade:.2f}")

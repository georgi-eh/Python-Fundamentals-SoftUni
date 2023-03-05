input_line = input()
courses = {}

while not input_line == "end":
    course, student = input_line.split(" : ")
    if course not in courses:
        courses[course] = []
        courses[course].append(student)
    else:
        courses[course].append(student)

    input_line = input()

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")

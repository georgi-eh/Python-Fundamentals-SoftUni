def add_lesson(schedule_list):
    if lesson not in schedule_list:
        schedule_list.append(lesson)


def insert_lesson(schedule_list, index_to_insert):
    if lesson not in schedule_list:
        schedule_list.insert(index_to_insert, lesson)


def remove_lesson(schedule_list):
    if lesson in schedule_list:
        if exercise in schedule_list:
            schedule_list.remove(exercise)
        schedule_list.remove(lesson)


def swap_lesson(schedule_list, lesson_swap):
    if lesson in schedule_list and lesson_swap in schedule_list:
        lesson_index = schedule_list.index(lesson)
        lesson_swap_index = schedule_list.index(lesson_swap)
        schedule_list[lesson_index] = lesson_swap
        schedule_list[lesson_swap_index] = lesson

    if exercise in schedule_list:
        schedule_list.remove(exercise)
        lesson_index = schedule_list.index(lesson)
        schedule_list.insert(lesson_index + 1, exercise)

    if exercise_to_swap in schedule_list:
        schedule_list.remove(exercise_to_swap)
        lesson_swap_index = schedule_list.index(lesson_swap)
        schedule_list.insert(lesson_swap_index + 1, exercise_to_swap)


def exercise_add(schedule_list):
    if lesson not in schedule_list:
        schedule_list.append(lesson)
        schedule_list.append(exercise)
    else:
        if exercise not in schedule_list:
            lesson_index = schedule_list.index(lesson)
            schedule_list.insert(lesson_index + 1, exercise)


schedule = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    action = command[0]
    lesson = command[1]
    exercise = f"{lesson}-Exercise"

    if action == "Add":
        add_lesson(schedule)

    elif action == "Insert":
        index = int(command[2])
        insert_lesson(schedule, index)

    elif action == "Remove":
        remove_lesson(schedule)

    elif action == "Swap":
        lesson_to_swap = command[2]
        exercise_to_swap = f"{lesson_to_swap}-Exercise"
        swap_lesson(schedule, lesson_to_swap)

    elif action == "Exercise":
        exercise_add(schedule)

    command = input()

for number in range(0, len(schedule)):
    print(f"{number + 1}.{schedule[number]}")

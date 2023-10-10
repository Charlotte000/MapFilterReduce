def get_statistics(students: list[dict], min_student_age: int = 21) -> tuple[list[dict], float, dict]:
    all_students = list(map(
        lambda student: { **student, 'average': sum(student['grades']) / len(student['grades']) },
        filter(
            lambda student: student['age'] >= min_student_age,
            students
        )
    ))

    average = sum(map(lambda student: student['average'], all_students)) / len(all_students)

    best_student = max(
        all_students,
        key=lambda student: student['average']
    )

    return (all_students, average, best_student)


students: list[dict] = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "David", "age": 19, "grades": [13, 80, 11, 88]},
    {"name": "Emily", "age": 23, "grades": [90, 23, 88, 21]},
    {"name": "Frank", "age": 20, "grades": [62, 79, 85, 35]},
    {"name": "Grace", "age": 21, "grades": [95, 92, 90, 94]},
    {"name": "Henry", "age": 22, "grades": [78, 82, 80, 65]},
    {"name": "Jack", "age": 20, "grades": [74, 88, 82, 54]},
    {"name": "Katie", "age": 21, "grades": [92, 91, 88, 93]},
    {"name": "Liam", "age": 23, "grades": [79, 85, 78, 87]},
    {"name": "Mia", "age": 20, "grades": [90, 61, 89, 94]},
    {"name": "Noah", "age": 21, "grades": [87, 88, 90, 85]},
    {"name": "Olivia", "age": 22, "grades": [74, 0, 89, 96]},
    {"name": "Peter", "age": 20, "grades": [85, 88, 90, 91]},
    {"name": "Quinn", "age": 21, "grades": [91, 78, 55, 92]},
    {"name": "Rachel", "age": 22, "grades": [20, 45, 34, 11]},
    {"name": "Sam", "age": 20, "grades": [86, 88, 92, 89]},
    {"name": "Tyler", "age": 21, "grades": [78, 92, 84, 91]},
    {"name": "Ursula", "age": 22, "grades": [72, 56, 88, 89]},
]

stats = get_statistics(students)
print(f'All students: {stats[0]}')
print(f'Average: {stats[1]}')
print(f'Best student: {stats[2]}')

def get_expenses_sum(users: list[dict], min_expenses_amount: int = 3):
    return sum(
        map(
            lambda user: sum(user['expenses']),
            filter(
                lambda user: len(user['expenses']) >= min_expenses_amount,
                users
            )
        )
    )


users = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [50, 75, 80, 100]},
    {"name": "Charlie", "expenses": [200, 300, 50, 150]},
    {"name": "David", "expenses": [400]},
    {"name": "Emily", "expenses": [120, 80, 90, 150]},
    {"name": "Frank", "expenses": [110, 130]},
    {"name": "Grace", "expenses": [150, 180, 220]},
    {"name": "Henry", "expenses": [90, 120, 110, 130]},
    {"name": "Ivy", "expenses": [70]},
    {"name": "Jack", "expenses": [120, 130, 110, 140]},
    {"name": "Katie", "expenses": [100, 120, 130, 110]},
    {"name": "Liam", "expenses": [80, 120, 100]},
    {"name": "Noah", "expenses": [110, 100, 120, 78, 130]},
    {"name": "Olivia", "expenses": [160, 150, 140, 170]},
    {"name": "Peter", "expenses": [120, 130, 140]},
    {"name": "Quinn", "expenses": [140, 130, 150, 120]},
    {"name": "Rachel", "expenses": [110, 120, 130, 100, 120, 140, 210, 150, 180]},
    {"name": "Sam", "expenses": [100, 120, 130]},
    {"name": "Tyler", "expenses": [130, 150]},
    {"name": "Ursula", "expenses": [140, 130, 150, 120]},
]

print(f'Expenses sum: {get_expenses_sum(users)}')

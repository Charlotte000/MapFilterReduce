def get_average_order(orders: list[dict], customer_id: int = 101):
    amounts = list(map(
        lambda order: order['amount'],
        filter(
            lambda order: order['customer_id'] == customer_id,
            orders
        )
    ))

    return sum(amounts) / len(amounts)


orders = [
    {"order_id": 1, "customer_id": 101, "amount": 150.0},
    {"order_id": 2, "customer_id": 102, "amount": 200.0},
    {"order_id": 3, "customer_id": 101, "amount": 75.0},
    {"order_id": 4, "customer_id": 103, "amount": 100.0},
    {"order_id": 5, "customer_id": 101, "amount": 50.0},
    {"order_id": 6, "customer_id": 102, "amount": 120.0},
    {"order_id": 7, "customer_id": 103, "amount": 80.0},
    {"order_id": 8, "customer_id": 102, "amount": 90.0},
    {"order_id": 9, "customer_id": 101, "amount": 110.0},
    {"order_id": 10, "customer_id": 104, "amount": 70.0},
    {"order_id": 11, "customer_id": 102, "amount": 130.0},
    {"order_id": 12, "customer_id": 101, "amount": 60.0},
    {"order_id": 13, "customer_id": 103, "amount": 95.0},
    {"order_id": 14, "customer_id": 104, "amount": 85.0},
    {"order_id": 15, "customer_id": 101, "amount": 40.0},
    {"order_id": 16, "customer_id": 102, "amount": 75.0},
    {"order_id": 17, "customer_id": 104, "amount": 100.0},
    {"order_id": 18, "customer_id": 103, "amount": 120.0},
    {"order_id": 19, "customer_id": 101, "amount": 55.0},
    {"order_id": 20, "customer_id": 102, "amount": 80.0},
]

print(f'Average order: {get_average_order(orders, 101)}')

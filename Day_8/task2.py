orders = ["pizza", "burger", "pasta", "sushi", "tacos"]
orders.pop()
print(orders[-1])
orders.pop(0)
print(orders[0])
cancelled = []
cancelled.append(orders[1])
orders.pop(1)
print(orders)
print(cancelled)
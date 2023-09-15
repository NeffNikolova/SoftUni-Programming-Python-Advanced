from collections import deque

available_food = int(input())
orders = deque([int(order) for order in input().split()])

print(max(orders))

while orders:
    if orders[0] <= available_food:
        available_food -= orders.popleft()
    else:
        print(f"Orders left: ", end='')
        print(*orders, sep=' ')
        break
else:
    print("Orders complete")
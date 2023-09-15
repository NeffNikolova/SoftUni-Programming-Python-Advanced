from collections import deque

customer = input()
queue = deque()
while customer != 'End':
    queue.append(customer)
    if customer == 'Paid':
        queue.pop()
        while queue:
            print(queue.popleft())
    customer = input()
else:
    print(f'{len(queue)} people remaining.')

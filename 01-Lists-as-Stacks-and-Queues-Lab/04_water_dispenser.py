from collections import deque
available_water = int(input())
name = input()
queue = deque()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()
while command != 'End':
    if command.startswith('refill'):
        available_water += int(command.split(' ')[-1])
    elif int(command) <= available_water:
        available_water -= int(command)
        print(f'{queue.popleft()} got water')
    elif int(command) > available_water:
        print(f'{queue.popleft()} must wait')
    command = input()
else:
    print(f'{available_water} liters left')

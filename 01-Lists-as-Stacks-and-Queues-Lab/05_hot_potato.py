from collections import deque

children_playing = deque(input().split())
toss_number = int(input()) - 1


while len(children_playing) > 1:
    children_playing.rotate(-toss_number)
    print(f'Removed {children_playing.popleft()}')
else:
    print(f'Last is {children_playing.popleft()}')

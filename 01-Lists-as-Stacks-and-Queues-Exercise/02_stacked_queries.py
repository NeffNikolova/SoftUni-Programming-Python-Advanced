
N = int(input())
stack = []

for entry in range(N):
    query = input()
    if query.startswith('1'):
        number = query.split()[1]
        stack.append(int(number))
    elif query == '2':
        if stack:
            stack.pop()
    elif query == '3':
        if stack:
            max_digit = max(stack)
            print(max_digit)
    elif query == '4':
        if stack:
            min_digit = min(stack)
            print(min_digit)

if stack:
    print(*stack[::-1], sep=', ')

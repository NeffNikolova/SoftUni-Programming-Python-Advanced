string = input()

stack = []
reverse_string = []
for char in string:
    stack.append(char)
while stack:
    reverse_string.append(stack.pop())

print(*reverse_string, sep='')
expression = input()

stack = []

for index in range(len(expression)):
    if expression[int(index)] == '(':
        stack.append(int(index))
    elif expression[int(index)] == ')':
        print(expression[(stack.pop()):int(index) + 1])


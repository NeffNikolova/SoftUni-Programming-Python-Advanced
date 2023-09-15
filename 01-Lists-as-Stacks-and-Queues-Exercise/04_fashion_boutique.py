boxed_clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
nr_racks = 1

while boxed_clothes_stack:
    if boxed_clothes_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= boxed_clothes_stack.pop()
    else:
        nr_racks += 1
        current_rack_capacity = rack_capacity

print(nr_racks)

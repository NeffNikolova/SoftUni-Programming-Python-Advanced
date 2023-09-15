# from collections import deque
#
# nr_pumps = int(input())
# pumps_data = []
# truck_petrol = 0
#
# for _ in range(nr_pumps):
#     petrol, distance_to_next = input().split()
#     pumps_data.append([int(petrol), int(distance_to_next)])
#
# pumps = deque(pumps_data)
#
# start_index = 0
# passed_pumps = 0
#
# while passed_pumps < nr_pumps:
#     for _ in range(nr_pumps):
#         truck_petrol += pumps[0][0]
#         truck_petrol -= pumps[0][1]
#         passed_pumps += 1
#         pumps.rotate(-1)
#         if truck_petrol < 0:
#             truck_petrol = 0
#             start_index += 1
#             break
#
# print(start_index)

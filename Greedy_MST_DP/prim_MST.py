from collections import defaultdict
import heapq
from random import choice,seed
def graph_input(text_file):
    adj_list = defaultdict(list)
    with open(text_file, 'r') as f:
        for line in f:
            arr = list(map(int, line.split()))
            adj_list[arr[0]].append((arr[1],arr[2]))
            adj_list[arr[1]].append((arr[0],arr[2]))
    return adj_list

def prim_MST(adj_list):
    seed(42)
    seen = {choice(list((adj_list.keys())))}
    edges_picked = []
    vertices_count= 1
    vertices_total = len(adj_list)
    total = 0

    #initialize heap
    queue = []
    for node in seen:
        for neighbor in adj_list[node]:
            heapq.heappush(queue, (neighbor[1],node,neighbor[0])) #queue's element is (dist, source, dest)

    while vertices_count < vertices_total:
        elem = heapq.heappop(queue)
        if elem[2] not in seen:
            seen.add(elem[2])
            edges_picked.append((elem[1],elem[2]))
            total += elem[0]
            vertices_count += 1

            for neighbor in adj_list[elem[2]]:
                if neighbor[0] not in seen:
                    heapq.heappush(queue, (neighbor[1], elem[2], neighbor[0]))
    
    return total
                    
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i][2] == target:
            return i
    return None


# graph_positive = {
#     'A': [('B', 4), ('C', 2)],
#     'B': [('A', 4), ('C', 1), ('D', 5)],
#     'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
#     'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
#     'E': [('C', 10), ('D', 2), ('F', 3)],
#     'F': [('D', 6), ('E', 3)]
# }

# graph_mixed = {
#     'A': [('B', -1), ('C', 4)],
#     'B': [('A', -1), ('C', 3), ('D', 2)],
#     'C': [('A', 4), ('B', 3), ('D', -2), ('E', 5)],
#     'D': [('B', 2), ('C', -2), ('E', -3)],
#     'E': [('C', 5), ('D', -3)]
# }

# print(prim_MST(graph_positive))
# print(prim_MST(graph_mixed))

a = graph_input('edges.txt')
print(prim_MST(a))
import random

def random_contraction(graph: dict): #assumes undirected graph
    while len(graph) > 2:
        keys = list(graph.keys())
        tail = random.choice(keys)
        head = random.choice(graph[tail])
        new_key = int(str(tail) + str(head))
        new_arr = []
        for elem in graph[head]:
            if elem != tail:
                new_arr.append(elem)
            graph[elem].remove(head)
        for elem in graph[tail]:
            if elem != head:
                new_arr.append(elem)
            graph[elem].remove(tail)
        for elem in new_arr:
            graph[elem].append(new_key)
        graph[new_key] = list(new_arr)
        del graph[head]
        del graph[tail]

'''
graph = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [1, 2, 3, 5],
    5: [4, 6, 7, 8],
    6: [5, 7, 8],
    7: [5, 6, 8],
    8: [5, 6, 7]
}
random_contraction(graph)
print(len(graph))
'''
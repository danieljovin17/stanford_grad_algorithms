import heapq
import random
from time import time
def dijkstra(graph, source):
    in_queue = set()
    res = dict()
    res[source] = 0
    queue = []
    for neighbor in graph[source]:
        v = graph[source][neighbor]
        heapq.heappush(queue,(v,source,neighbor)) #distance, source, destination
        in_queue.add(neighbor)
    while len(res) < len(graph):
        elem = heapq.heappop(queue) #elem = (distance, source, destination)
        res[elem[2]] = elem[0] + res[elem[1]]
        for neighbor in graph[elem[2]]:
            if res.get(neighbor) == None:
                v = graph[elem[2]][neighbor]
                if neighbor not in in_queue:
                    heapq.heappush(queue,(v,elem[2],neighbor))
                    in_queue.add(neighbor)
                else:
                    x = search(queue,neighbor)
                    if v < queue[x][0]:
                        del queue[x]
                        heapq.heappush(queue,(v,elem[2],neighbor))
        in_queue.remove(elem[2])
    return res
'''
#Version 1 of Dijkstra attempt: uses path memorization to prevent repeated paths
def dijkstra_bottleneck(graph, source, target):
    res = dict()
    res[source] = 0
    queue = []
    for neighbor in graph[source]:
        v = graph[source][neighbor]
        heapq.heappush(queue,[v,neighbor,{source,neighbor}]) #bottleneck, dest, path
    while queue:
        elem = heapq.heappop(queue) #elem = (bottleneck, dest, path)
        if res.get(elem[1]) != None:
            res[elem[1]] = min(elem[0],res[elem[1]])
        else:
            res[elem[1]] = elem[0]
        if elem[2] == target:
            return res[target]
        for neighbor in graph[elem[1]]:
            if neighbor not in elem[2]:
                v = max(graph[elem[1]][neighbor], res[elem[1]])
                path = elem[2].copy()
                path.add(neighbor)
                heapq.heappush(queue,[v,neighbor,path])
    return res
'''
#Version 2 of Dijkstra attempt: uses edge memorization to prevent repeated paths
def dijkstra_bottleneck2(graph, source, target):
    res = dict()
    res[source] = 0
    queue = []
    edges_seen = set()
    # t1_t2 = 0
    # t2_t1 = 0
    # t1 = time()
    # t2 = time()
    for neighbor in graph[source]:
        v = graph[source][neighbor]
        edge = tuple(sorted([source,neighbor]))
        heapq.heappush(queue,(v,neighbor, edge)) #bottleneck, dest, edge
        edges_seen.add(edge)
    while queue:
        elem = heapq.heappop(queue) #elem = (bottleneck, dest, edge)
        if res.get(elem[1]) != None:
            res[elem[1]] = min(elem[0],res[elem[1]])
        else:
            res[elem[1]] = elem[0]
        if elem[1] == target:
            # print("non heappush operations sum", t1_t2)
            # print("heappush operations sum", t2_t1)
            return res[target]
        for neighbor in graph[elem[1]]:
            edge = tuple(sorted([elem[1],neighbor]))
            if edge not in edges_seen:
                v = max(graph[elem[1]][neighbor], res[elem[1]])
                # t1 = time()
                # t1_t2 += (t1-t2)
                heapq.heappush(queue,(v,neighbor,edge))
                # t2 = time()
                # t2_t1 += (t2-t1)
                edges_seen.add(edge)
    # print("non heappush operations sum", t1_t2)
    # print("heappush operations sum", t2_t1)
    return res[target]

def search(arr,node):
    for i in range(len(arr)):
        if node == arr[i][2]:
            return i
    return None
        
        
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3, 'G': 1},
    'G': {'F': 1}
}

bottleneck_graph = {
    'S': {'A': 10, 'B': 1},
    'A': {'S': 10, 'C': 2, 'D': 8},
    'B': {'S': 1, 'C': 15, 'E': 3},
    'C': {'A': 2, 'B': 15, 'D': 4, 'F': 12},
    'D': {'A': 8, 'C': 4, 'T': 5},
    'E': {'B': 3, 'F': 6, 'T': 20},
    'F': {'C': 12, 'E': 6, 'T': 7},
    'T': {'D': 5, 'E': 20, 'F': 7}
}

def generate_large_graph(num_vertices=100, edge_probability=0.05, max_weight=20):
    """
    Generate a random weighted graph with guaranteed connectivity
    
    Args:
        num_vertices: Number of vertices (default 100)
        edge_probability: Probability of edge between any two vertices
        max_weight: Maximum edge weight
    """
    
    # Create vertices labeled 0 to 99
    vertices = list(range(num_vertices))
    graph = {v: {} for v in vertices}
    
    # First, create a spanning tree to ensure connectivity
    # This guarantees the graph is connected
    unconnected = set(vertices[1:])  # All except vertex 0
    connected = {0}  # Start with vertex 0
    
    while unconnected:
        # Pick a random vertex from connected set
        from_vertex = random.choice(list(connected))
        # Pick a random vertex from unconnected set
        to_vertex = random.choice(list(unconnected))
        
        # Add edge with random weight
        weight = random.randint(1, max_weight)
        graph[from_vertex][to_vertex] = weight
        graph[to_vertex][from_vertex] = weight
        
        # Move vertex to connected set
        connected.add(to_vertex)
        unconnected.remove(to_vertex)
    
    # Add additional random edges for more interesting paths
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            # Skip if edge already exists
            if j in graph[i]:
                continue
                
            # Add edge with given probability
            if random.random() < edge_probability:
                weight = random.randint(1, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight
    
    return graph
a = 10000
g1 = generate_large_graph(num_vertices=a)
# print(g1)
print(dijkstra_bottleneck2(g1,1,a-5))
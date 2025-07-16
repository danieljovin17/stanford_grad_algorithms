def reverse_graph(graph: dict):
    reversed_graph = dict()
    for k in graph.keys():
        reversed_graph[k] = []
    for k,v in graph.items():
        for node in v:
            reversed_graph[node].append(k)
    return reversed_graph

def count_scc(graph: dict):
    r_graph = reverse_graph(graph)
    r_finishing_seq = []
    seen = set()

    def dfs(graph, node, mode):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(graph,neighbor,mode)
        if not mode:
            r_finishing_seq.append(node)
    
    for node in r_graph:
        if node not in seen:
            seen.add(node)
            dfs(r_graph,node,False)
            
    count = 0
    seen.clear()
    for i in range(1,len(r_finishing_seq)+1):
        if r_finishing_seq[-i] not in seen:
            seen.add(r_finishing_seq[-i])
            dfs(graph,r_finishing_seq[-i],True)
            count += 1
    return count

graph = {
    0: [1],
    1: [2, 4],
    2: [3, 6],
    3: [0],
    4: [5],
    5: [6],
    6: [7],
    7: [8],
    8: [9],
    9: [6],
    10: [11],
    11: [12],
    12: [10],
    13: []
}

print(count_scc(graph))
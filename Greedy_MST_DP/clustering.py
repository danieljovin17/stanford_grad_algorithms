from collections import defaultdict
import heapq
from disjoint_set import DisjointSet
def graph_input(text_file):
    adj_list = defaultdict(list)
    with open(text_file, 'r') as f:
        for line in f:
            arr = list(map(int, line.split()))
            adj_list[arr[0]].append((arr[1],arr[2]))
            adj_list[arr[1]].append((arr[0],arr[2]))
    return adj_list

def graph_input_edges_heap(text_file):
    minHeap = []
    member_set = set()
    with open(text_file, 'r') as f:
        for line in f:
            arr = line.strip().split()
            elem = (int(arr[2]), arr[0], arr[1])
            minHeap.append(elem)
            member_set.add(elem[1])
            member_set.add(elem[2])
    heapq.heapify(minHeap)
    return minHeap, member_set

def k_clustering(edge_heap, member_list,  k = 4):
    ds = DisjointSet.from_iterable(member_list)
    length = len(ds)
    while length > k: #clustering algorithm
        elem = heapq.heappop(edge_heap)
        if not ds.connected(elem[1], elem[2]):
            ds.union(elem[1], elem[2])
            length -= 1

    d = dict()
    while edge_heap: #find max distance between any two clusters
        elem = heapq.heappop(edge_heap)
        if not ds.connected(elem[1], elem[2]):
            tmp = tuple(sorted([ds.find(elem[1]),ds.find(elem[2])]))
            if not d.get(tmp):
                d[tmp] = elem[0]
            else:
                d[tmp] = min(elem[0], d[tmp])
    return max(list(d.values()))
a, b = graph_input_edges_heap('clustering1.txt')
print(k_clustering(a,b))

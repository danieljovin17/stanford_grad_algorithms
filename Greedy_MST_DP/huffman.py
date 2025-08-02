import heapq
from time import time

class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
    
    def __repr__(self):
        return self.value

def heapify_input(text_file):
    queue = []
    with open(text_file, 'r') as f:
        i = 0
        for line in f:
            queue.append((int(line.strip()), i))
            i += 1
        heapq.heapify(queue)

def heappush_input(text_file):
    queue = []
    with open(text_file, 'r') as f:
        i = 0
        for line in f:
            heapq.heappush(queue, (int(line.strip()), str(i)))
            i += 1
    return queue

def dfs(root):
    if not root.left and not root.right:
        return 0
    else:
        return 1 + max(dfs(root.left), dfs(root.right))

def main():
    queue = heappush_input('huffman.txt')
    d = dict() #key:value = element:Node
    while len(queue)>1:
        elem1 = heapq.heappop(queue)
        elem2 = heapq.heappop(queue)
        empty_node = Node(value = elem1[1]+"_"+elem2[1])
        if d.get(elem1[1]):
            node1 = d.get(elem1[1])
        else:
            node1 = Node(value = elem1[1], parent = empty_node)

        if d.get(elem2[1]):
            node2 = d.get(elem2[1])
        else:
            node2 = Node(value = elem2[1], parent = empty_node)
        empty_node.left = node1
        empty_node.right = node2
        d[empty_node.value] = empty_node
        heapq.heappush(queue, (elem1[0]+elem2[0],empty_node.value))
    
    print(dfs(d[heapq.heappop(queue)[1]]))


if __name__ == '__main__':
    main()
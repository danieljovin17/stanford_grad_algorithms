import sys
from functools import cache
from time import time
sys.setrecursionlimit(5000)

CAPACITY = 2000000
def text_input(text_file):
    arr = []
    with open(text_file, 'r') as f:
        for line in f:
            arr.append(tuple(map(int,line.split()))) #stores v,w
    return arr

arr = text_input('knapsack_big.txt') #(value,weight)
#arr = [(60, 10), (100, 20), (120, 30), (40, 15), (80, 25), (30, 5)]

d = dict()
def recursive_knapsack(i, capacity):
    if i >= len(arr):
        return 0
    else:
        if x := d.get((i,capacity)):
            return x
        elif capacity-arr[i][1] >= 0:
            d[(i,capacity)] = max(recursive_knapsack(i+1,capacity-arr[i][1])+arr[i][0],recursive_knapsack(i+1,capacity))
            return d[(i,capacity)] 
        else:
            d[(i,capacity)] = recursive_knapsack(i+1,capacity)
            return d[(i,capacity)]
        
@cache
def recursive_knapsack2(i, capacity):
    if i >= len(arr):
        return 0
    else:
        if capacity-arr[i][1] >= 0:
            return max(recursive_knapsack2(i+1,capacity-arr[i][1])+arr[i][0],recursive_knapsack2(i+1,capacity))
        else:
            return recursive_knapsack2(i+1,capacity)

t1 = time()
print(recursive_knapsack(0,CAPACITY))
t2 = time()
print(f'time taken: {t2-t1}')

t1 = time()
print(recursive_knapsack2(0,CAPACITY))
t2 = time()
print(f'time taken: {t2-t1}')
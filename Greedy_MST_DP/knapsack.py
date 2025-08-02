from pprint import pprint
CAPACITY = 10000
def text_input(text_file):
    arr = []
    with open(text_file, 'r') as f:
        for line in f:
            arr.append(tuple(map(int,line.split()))) #stores v,w
    return arr

def dp():
    arr = text_input('knapsack1.txt')
    #arr = [(60, 10), (100, 20), (120, 30), (40, 15), (80, 25), (30, 5)]
    cap = [0 for _ in range(0,CAPACITY+1)]
    dp = []
    for _ in range(len(arr)+1):
        dp.append(cap[:])
    
    #dp[n][W]
    for i in range(1,len(arr)+1):
        for w in range(0,CAPACITY+1):
            if w-arr[i-1][1] >= 0:
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-arr[i-1][1]]+arr[i-1][0])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[len(arr)][CAPACITY]

def dp_reverse():
    arr,ans = dp()
    i = len(ans)
    res = []
    capacity = CAPACITY
    while i > 1:
        if ans[i-1][capacity] == ans[i-2][capacity]:
            i -= 1
        else:
            res.append(i-1)
            capacity -= arr[i-2][1]
            i-=1
            if capacity == 0:
                break
    print(sorted(res))

print(dp())
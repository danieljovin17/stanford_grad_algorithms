def input_array(text_file):
    arr = []
    with open(text_file, 'r') as f:
        for line in f:
            arr.append(int(line.strip()))
    return arr

def mwis(arr):
    dp = [0 for _ in range(len(arr)+1)]
    dp[1] = arr[0]
    for i in range(2,len(arr)+1):
        dp[i] = max(dp[i-1],dp[i-2]+arr[i-1])
    return dp[-1]

arr = input_array('mwis.txt')
print(mwis(arr))

d = dict()
def dp(i):
    if i == 0:
        return arr[i]
    elif i == 1:
        return max(arr[0], arr[1])
    elif x := d.get(i):
        return x 
    else:
        x = max(dp(i-1), dp(i-2)+arr[i])
        d[i] = x
        return x 
    
print(dp(len(arr)-1))
import random

#this implementation takes extra space with naive pivot selection
def qSort_naive(m):
    if len(m) <= 1:
        return m
    else:
        pivot = [m[-1]]
        L = []
        R = []
        for i in range(len(m)-1):
            if m[i] <= pivot[0]:
                L.append(m[i])
            else:
                R.append(m[i])
        return qSort_naive(L) + pivot + qSort_naive(R)
    
#this implementation takes extra space with randomized pivot selection
def qSort_random(m):
    length = len(m) 
    if length <= 1:
        return m
    else:
        pivot_index = int(random.uniform(0,length))
        pivot = [m[pivot_index]]
        L = []
        R = []
        for i in range(length):
            if i == pivot_index:
                continue
            elif m[i] <= pivot[0]:
                L.append(m[i])
            else:
                R.append(m[i])
        return qSort_random(L) + pivot + qSort_random(R)
    
#this implementation takes no extra space with randomized pivot selection
def qSort(m):
    length = len(m) 
    def helper(m,L,R):
        if R-L <= 1:
            return m
        elif R - L == 2:
            if m[L] > m[L+1]:
                m[L+1], m[L] = m[L], m[L+1]
        else:
            pivot_index = int(random.uniform(L,R))
            m[L], m[pivot_index] = m[pivot_index], m[L] #swap pivot to the first element
            i = L+1
            for j in range(L+1,R):
                if m[j] <= m[L]:
                    m[i] , m[j] = m[j] , m[i]
                    i += 1 #i will be at the left-most element larger than pivot
            m[L],m[i-1] = m[i-1],m[L] 
            helper(m,L,i-1)
            helper(m,i,R)
    helper(m,0,length)
    
m = [123,5,123,1,2,4,3453,435,1241,34,-2]
qSort(m)
print(m)

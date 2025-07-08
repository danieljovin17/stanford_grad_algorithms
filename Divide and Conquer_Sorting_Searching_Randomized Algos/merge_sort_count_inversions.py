def merge_sort(L:list[int]) -> list[int]: #does not sort in place
    length = len(L)
    if length < 2:
        return L
    else:
        a = merge_sort(L[:length//2])
        b = merge_sort(L[length//2:])
        length_a = len(a)
        length_b = len(b)
        left = 0
        right = 0
        c = []
        while left < length_a and right < length_b:
            if a[left] <= b[right]:
                c.append(a[left])
                left+=1
            else:
                c.append(b[right])
                right += 1
        if left == length_a:
            c.extend(b[right:])
        elif right == length_b:
            c.extend(a[left:])
        return c
    
def merge_sort_count_inversion(L:list[int]) -> tuple[int,list[int]]: 
    length = len(L)
    if length < 2:
        return (0,L)
    else:
        left_inv, a = merge_sort_count_inversion(L[:length//2])
        right_inv, b = merge_sort_count_inversion(L[length//2:])
        split = 0
        length_a = len(a)
        length_b = len(b)
        left = 0
        right = 0
        c = []
        while left < length_a and right < length_b:
            if a[left] <= b[right]:
                c.append(a[left])
                left+=1
            else:
                c.append(b[right])
                right += 1
                split += (length_a-left)
        if left == length_a:
            c.extend(b[right:])
        elif right == length_b:
            c.extend(a[left:])
        return (split+left_inv+right_inv,c)
    
'''
def matrix_multiply(m:list[list[int]], n:list[list[int]]) -> list[list[int]]: #for square matrices of even sizes only, unfinished
    matrix_size = len(m)
    sub_size = matrix_size//2
    def sub_matrix_generator(matrix):
        a,b,c,d = [],[],[],[]
        for i in range(len(matrix)):
            row1 = []
            row2 = []
            for j in range(len(matrix[0])):
                if j < sub_size:
                    row1.append(matrix[i][j])
                else:
                    row2.append(matrix[i][j])
            if i < sub_size:
                a.append(row1[:])
                b.append(row2[:])
            else:
                c.append(row1[:])
                d.append(row2[:])
        return a,b,c,d
        
    if matrix_size == 1: #matrix of single element
        return [[m[0][0]*n[0][0]]]
    else:
        a,b,c,d = sub_matrix_generator(m) #works
        e,f,g,h = sub_matrix_generator(n) #works
        #need to define matrix addition and subtraction
        p1= 
        p2=
        p3=
        p4=
        p5=
        p6=
        p7=
        #combine the matrices

M = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
print(matrix_multiply(M,[]))
'''
from typing import Optional
class HeapOperations(): #static methods only as it will just interact with python lists
    @staticmethod
    def parent_position(position):
        return (position - 1)//2 if position else 0
    
    @staticmethod
    def children_position(position):
        return 2*position+1, 2*position+2
    
    @staticmethod
    def heapify(ls):
        '''
        Arranges list/array to obey heap properties. Future Updates: To check if a given array is eligible to be transformed.
        '''
        length = len(ls)

        def getter(ls, position) -> Optional[int|float]:
            if position >= length:
                return None
            
            x = ls[position]
            if type(x) in (int, float):
                return x
            elif type(x) in (list, tuple):
                return x[0]
            else:
                raise ValueError("Key is not numeric!")
            
        def helper(i):
            parent = HeapOperations.parent_position(i)
            left, right = HeapOperations.children_position(i)
            if left >= length: #out of bounds
                return
            get_left = getter(ls, left)
            get_i = getter(ls, i)
            get_right = getter(ls, right)
            if get_left == None and get_right == None: #leaf node
                return
            elif get_right == None: #if right-side is out-of bounds, it will fall here also
                if get_left < get_i:
                    ls[left], ls[i] = ls[i], ls[left]
                    helper(parent) if parent != i else 0
            elif get_left == None:
                if get_right < get_i:
                    ls[right], ls[i] = ls[i], ls[right]
                    helper(parent) if parent != i else 0
            else:
                while (get_left < get_i) or (get_right < get_i):
                    if get_left<=get_right:
                        ls[left], ls[i] = ls[i], ls[left]
                        helper(parent) if parent != i else 0
                        get_left = getter(ls, left)
                        get_i = getter(ls, i)
                    else:
                        ls[right], ls[i] = ls[i], ls[right]
                        helper(parent) if parent != i else 0
                        get_i = getter(ls, i)
                        get_right = getter(ls, right)
            helper(left)
            helper(right)
        helper(0)

    @staticmethod
    def pop(ls): #swap with last node, and then heapify (O(n)) (or write bubble-down code (O(lgn)))
        #swap first and last node
        ls[0], ls[-1] = ls[-1], ls[0]
        elem = ls.pop()
        i = 0
        left, right = HeapOperations.children_position(i)
        length = len(ls)
        while (left<length and right<length) and ((ls[i] > ls[left]) or (ls[i] > ls[right])):
            if ls[left] <= ls[right]:
                ls[left], ls[i] = ls[i], ls[left]
                i = left
                left, right = HeapOperations.children_position(i)
            else:
                ls[right], ls[i] = ls[i], ls[right]
                i = right
                left, right = HeapOperations.children_position(i)
        return elem
        
    @staticmethod
    def insert(ls, elem): #insert at the end, and swap with parents if needed
        ls.append(elem)
        length = len(ls)
        parent = HeapOperations.parent_position(length-1)
        i = length-1
        while ls[parent] > ls[i]:
            ls[parent], ls[i] = ls[i], ls[parent]
            i = parent
            parent = HeapOperations.parent_position(parent)

    @staticmethod
    def delete(ls, i): #swap with last node, and then heapify (O(n)) (or write bubble-down code (O(lgn)))
        ls[i], ls[-1] = ls[-1], ls[i]
        elem = ls.pop()
        left, right = HeapOperations.children_position(i)
        length = len(ls)
        while (left<length and right<length) and ((ls[i] > ls[left]) or (ls[i] > ls[right])):
            if ls[left] <= ls[right]:
                ls[left], ls[i] = ls[i], ls[left]
                i = left
                left, right = HeapOperations.children_position(i)
            else:
                ls[right], ls[i] = ls[i], ls[right]
                i = right
                left, right = HeapOperations.children_position(i)
        return elem
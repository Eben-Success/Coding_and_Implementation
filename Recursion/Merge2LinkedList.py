def SortedMerge(Node A, Node B):
    if (A == null): return B
    if (B == null): return A
    
    if (A.data < A.data):
        A.next = SortedMerge(A.next, B)
        return A
    else:
        B.next = SortedMerge(A, B.next)
        return B
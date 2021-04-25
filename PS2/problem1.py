

def local_min(A: [int]) -> int:
    # base case: if the size of array is 1, return the only elemet
    # if the size is 2, return the smaller element
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        return min(A)
    
    # choose the middle element in the array as the pivot
    pivot = len(A) // 2
    # if the pivot is already a local minimum, return it
    if A[pivot-1] >= A[pivot] <= A[pivot+1]:
        return A[pivot]
    # else, do recursive call on the partition of array with the smaller element,
    # not including the pivot, since that partition is guaranteed to have a local minimum
    if A[pivot-1] < A[pivot+1]:
        return local_min(A[:pivot])  # since end index is not included in list slicing
    else:
        return local_min(A[pivot+1:])
    
    
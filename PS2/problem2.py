
def find_median(vector1, vector2, n):
    # base case: if n is small (we chose 2 here), simply use a brute force algorithm
    if n <= 2:
        union = sorted(vector1 + vector2)
        # size of union vector will be either 2 or 4, depending on the value of n
        size = len(union)
        # the median of the two (small) vectors is the average of 
        # the middle two elements
        return (union[size/2] + union[size/2-1]) / 2
    
    # find the median of each vector. Since we know that the two vectors are sorted,
    # the median is simply the middle element 
    median1 = len(vector1) // 2
    median2 = len(vector2) // 2
    if n % 2 == 0:
        # if n is even, need to shift the index in one vector by one so that,
        # when we divide the vectors, their size, n, is still equal
        median2 -= 1
    
    if vector1[median1] < vector2[median2]:
        # in this case, the median will be in the following paritions:
        # vector1: from index of median1 to the end of vector
        # vector2: from beginning to index of median2
        # divide the vector into these partitions and do recursion
        partition1 = vector1[median1:]
        partition2 = vector2[:median2+1]
    else:
        # in this case, we parition the vectors similarly, but in the opposite 
        # directions
        partition1 = vector1[:median1+1]
        partition2 = vector2[median2:]
    # recursion step
    return find_median(partition1, partition2, len(partition1))

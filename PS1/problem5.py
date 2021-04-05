def have_common_key(A: MaxHeap, B: MaxHeap, n: int) -> bool:
    while n > 0:
        # get the max element of each max heap and compare them
        max_A = A.max()
        max_B = B.max()
        if max_A == max_B:
            # common key found
            return True
        try:
            # extract the maximum element of the max heap that has a greater max value
            if max_A > max_B:
                A.extractMax()
            else:
                B.extractMax()
        except Exception:
            # assume that extractMax() will throw an exception if the max heap
            # becomes empty, in this case there is no common key
            return False
        # decrement n since we removed an element
        n -= 1
    # both max heap becomes empty (n == 0), also indicates no common key
    return False

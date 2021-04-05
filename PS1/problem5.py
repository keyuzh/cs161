def have_common_key(A: MaxHeap, B: MaxHeap, n: int) -> bool:
    try:
        while n > 0:
            # get the max element of each max heap and compare them
            max_A = A.max()
            max_B = B.max()
            if max_A == max_B:
                # common key found
                return True
            # extract max from whichever max heap that has larger max value
            if max_A > max_B:
                A.extractMax()
            else:
                B.extractMax()
            # decrement n since we removed an element
            n -= 1
    except Exception:
        # assume that max() and extractMax() will throw an exception if the max heap
        # becomes empty, in this case there is no common key
        return False
    # if both max heap becomes empty (n == 0), also indicates no common key
    return False

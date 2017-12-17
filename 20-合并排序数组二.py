def mergeSortedArray(A, m, B, n):
    for i in range(n):
        A[m + i] = B[i]
    A.sort()
    return A


print(mergeSortedArray([1, 2, 3], 3, [4, 5], 2))

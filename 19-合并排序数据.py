def mergeSortedArray(A, B):
    A.extend(B)
    A.sort()
    return A

print(mergeSortedArray([1, 2, 3, 4], [2, 4, 6, 8]))
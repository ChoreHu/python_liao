# -*- coding: utf-8 -*-
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0], L[0])
    else:
        min = max = L[0]
        for v in L:
            if v < min:
                min = v
            elif v > max:
                max = v
        return (min, max)
    return (None, None)


print(findMinAndMax([7, 1, 3, 9, 5]))
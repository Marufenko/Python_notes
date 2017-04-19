'''
Merge sort algorithm:
1. If list is of length 0 or 1, already sorted
2. If list has more than one element, split into two lists, and sort each
3. Merge results:
    1. To merge, just look at first element of each, move smaller to end of the result
    2. When one list is empty, just copy rest of other list
'''

import operator

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right[j])):
        result.append(right[j])
        j += 1
    return result


def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:] # return copy of list
    else:
        middle = int(len(L)/2)
        left   = mergeSort(L[:middle], compare)
        right  = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
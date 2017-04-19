'''
Binary search algorithm (applied for sorted list):
1. Pick an index, i, that divides list in half
2. Ask if L[i] == e
3. If not, ask L[i] larger or smaller than e
4. Depend on answer, search left or right of L for e.
'''
def search(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = low + int((high-low)/2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
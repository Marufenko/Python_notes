'''
Selection sort algorithm:
1. Find the smallest element in the list and swap it with a first element
2. Take the remained of the list, find the smallest element and swap it with a second element.
3. Keep doing that until we've done the overall search.
'''

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal  = L[i]
        j = i + 1
        while j < len(L):
            # find smallest value to right of i
            if minVal > L[j]:
                minIndx = j
                minVal  = L[j]
            j += 1
        # switch
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
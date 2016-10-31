def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N=len(items)
    for i in range(3**N):
        bag1 =[]
        bag2 =[]

# n is a local variable that we repeatedly divide by 3
# in the loop. It is also fine to use i directly.
        n=i
        for j in range(N):
            a=n%3 # Extract the least significant digit.
            if a==1:
                bag1.append(items[j])
            elif a==2:
                bag2.append(items[j])
            n=n//3
        yield(bag1, bag2)

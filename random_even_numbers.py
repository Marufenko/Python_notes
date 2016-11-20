import random
def stochasticNumber():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    list = [x for x in range(9,21) if x%2 == 0]
    return random.choice(list)

def drawing_without_replacement_sim(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    """

    totalTry = 0
    successfulTry = 0

    for i in range(numTrials):
        totalTry += 1
        test = one_try()
        if test == True:
            successfulTry += 1

    return float(successfulTry) / float(totalTry)


def one_try():
    """
    function perform separate simulation
    """

    # let's count numbers 1-4 are red, 5-8 are green

    import random

    bucket = [1, 2, 3, 4, 5, 6, 7, 8]  # 1-4 are green, 5-8 are red (or vice versa)
    result = []
    for i in range(3):
        a = random.choice(bucket)
        result.append(a)
        bucket.remove(a)

    if (
        result[0] in [1, 2, 3, 4]
        and result[1] in [1, 2, 3, 4]
        and result[2] in [1, 2, 3, 4]
    ):
        return True
    if (
        result[0] in [5, 6, 7, 8]
        and result[1] in [5, 6, 7, 8]
        and result[2] in [5, 6, 7, 8]
    ):
        return True
    else:
        return False


print(drawing_without_replacement_sim(10000))

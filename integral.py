def integral(leftBorder, rightBorder, step):
    """
    function calculates intergal of 'function' on appropriate range with specified step of accuracy
    leftBorder  - float
    rightBorder - float
    step        - float
    """
    result = 0
    point = leftBorder
    while point < rightBorder:
        x = point
        result += float(calc(x)) * step
        point += step

    return result


def calc(x):
    """
    put here function
    """
    return (2 + ((2.75 * x) ** 3.2)) ** 0.5


print(integral(0, 7, 0.000005))

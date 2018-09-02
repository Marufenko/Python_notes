def main():
    positive_result(discriminant(4, 6, 5))


def discriminant(a, b, c):
    return (b**2) - (4*a*c)


def positive_result(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() reslt isn't >= 0"
        return result
    # wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper


if __name__ == "__main__":
    main()
def positive_result(function):
    def wrapper(*args, **kwargs):
        for i in args:
            print(i)
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() reslt isn't >= 0"
        return result + 1

    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper


def main():
    print(discriminant(4, 6, 5))


@positive_result
def discriminant(a, b, c):
    return 1


if __name__ == "__main__":
    main()

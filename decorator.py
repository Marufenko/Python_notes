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


class TestObject(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.name = self.__class__.__name__


def assert_if_exists(func):
    def wrapper(msg, attribute, *attr):
        g = func.__globals__

        try:
            g["actual"] = getattr(msg, attribute)
        except AttributeError:
            print(f"{msg.name} does not have attribute: {attribute}")
            return

        func(msg, attribute, *attr)
    return wrapper


@assert_if_exists
def assert_equal(msg=None, attribute=None, actual=None, expected=None):
    print(f"Actual: {actual}, Expected: {expected}, Validation: {actual == expected}")


@assert_if_exists
def assert_in_seq(msg, attribute, expected):
    print(f"Actual: {actual}, Expected: {expected}, Validation: {actual in expected}")


@assert_if_exists
def assert_non_none(msg, attribute):
    print(f"Actual: {actual}, Validation: {actual is not None}")


@positive_result
def discriminant(a, b, c):
    return 1


def main():
    print(discriminant(4, 6, 5))

    test = TestObject(x=7, y=5, z=3)

    assert_equal(test, "x", 7)
    assert_equal(test, "a", 0)
    assert_equal(test, "y", 7)

    assert_in_seq(test, "z", [1, 2, 3])
    assert_in_seq(test, "z", [1, 2])
    assert_in_seq(test, "a", [1, 2])

    assert_non_none(test, "x")
    assert_non_none(test, "a")


if __name__ == "__main__":
    main()

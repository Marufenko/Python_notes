def main():
    for i in fun_list(11):
        print(i)
    print("=============")
    for j in fun_generator(11):
        print(j)


def fun_list(fun_range: int):
    test_list = []
    for i in range(1, fun_range):
        test_list.append(2**i)
    return test_list


def fun_generator(fun_range: int):
    i = 1
    while i < fun_range:
        yield 2**i
        i += 1


if __name__ == "__main__":
    main()

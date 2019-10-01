from delayed_assert import expect, assert_expectations


def main():
    expect(1 == 1)
    expect(1 == 2)
    expect(1 == 3)
    expect(1 == 5)
    expect(1 == 6)
    assert_expectations()


if __name__ == "__main__":
    main()

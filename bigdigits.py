# tool transform provided digits to huge ones
# run this tool with int argument

import sys


def main(input_ints):
    assert input_ints.isdigit(), "Input should contains only Ints, not char, not space"

    numbers = [
        [" *** ", "*   *", "*   *", "*   *", "*   *", "*   *", " *** "],
        [" * ", "** ", " * ", " * ", " * ", " * ", "***"],
        [" *** ", "*   *", "*   *", "  *  ", " *   ", "*    ", "*****"],
        [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "],
        ["   * ", "  ** ", " * * ", "*  * ", "*****", "   * ", "   * "],
        ["*****", "*    ", "*    ", "**** ", "    *", "*   *", " *** "],
        [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "],
        ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "],
        [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "],
        [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"],
    ]

    for j in range(7):
        row = ""
        for i in input_ints:
            pre_row = numbers[int(i)][j]
            for k in pre_row:
                if k == " ":
                    row += k
                else:
                    row += i
            row += " "
        print(row)


if __name__ == "__main__":
    main("12358")

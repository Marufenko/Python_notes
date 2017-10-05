#!/usr/bin/env python3

import argparse

def main():
    print(process_options())

def process_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--hidden', dest='hidden', action='store_true',
                        help='show hidden files [default: off]')
    parser.add_argument('-m', '--modified', dest='modified', action='store_true',
                        help='show last modified date/time [default: off]')
    order_list = ['name', 'n', 'modified', 'm', 'size', 's']
    parser.add_argument('-o', '--order', dest='order', choices=order_list,
                        help="order by ({0}) [default: name]".format(
                            ', '.join(["'" + x + "'" for x in order_list])))
    parser.add_argument('-r', '--recursive', dest='recursive', action='store_true',
                        help='recurse into subdirectories [default: off]')
    parser.add_argument('-s', '--sizes', dest='sizes', action='store_true',
                        help='show sizes [default: off]')

    parser.set_defaults(order=order_list[0])
    args = parser.parse_args()
    if not args:
        args = ["."]
    return args

if __name__ == '__main__':
    main()
def recursion_for_polindrome(str):
    if len(str) <= 1:
        print('True')
    elif str[0] == str[-1]:
        recursion_for_polindrome(str[1:-1])
    else:
        print('False')

if __name__ == '__main__':
    recursion_for_polindrome('abbcbba')
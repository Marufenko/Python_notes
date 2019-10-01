def function(L):

    """
    L - string or list of charecters (){}[]
    function analisys L 'is it balances':
    ([]) - TRUE
    ([)] - FALSE
    """

    char_list = []
    for char in L:
        if char in [")", "]", "}"] and len(char_list) == 0:
            return False
        elif char == "(":
            char_list.append(")")
        elif char == "[":
            char_list.append("]")
        elif char == "{":
            char_list.append("}")
        elif char == char_list[-1]:
            char_list.pop()
        elif char != char_list[-1]:
            return False
        # print "char: " + char + " char_list: " + str(char_list)
    return True


print(function("(()())"))

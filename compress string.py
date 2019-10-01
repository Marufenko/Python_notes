def compress(string):
    # compress row from "aaaaaaaaabbc" to "a9b2c1"
    dictionary = {}
    result = ""

    for char in string:
        if char not in dictionary.keys():
            dictionary[char] = 1
        else:
            dictionary[char] = dictionary[char] + 1

    for key in dictionary.keys():
        result += str(key) + str(dictionary[key])

    return result

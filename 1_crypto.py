def main(inputString):

    result = inputString

    for i in [' ', '.', ',', ':', ';', '\'', '!', '?', '(', ')']:
        result = result.replace(i, '')

    print(result)

if __name__ == "__main__":
    main("!!hello . , : ; '! ? ( ) world!!")
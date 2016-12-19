import re
import codecs

def wordsCounting(fileName,firstWord,lastWord):
    '''
    function calculates TOP_COUNT most common words in specified range batween firstWord,lastWord and prints it
    '''

    name = fileName
    handle = codecs.open(name,"r","utf-8")
    text = handle.read()
    words = text.split()

    # 'counts' disc is created with word/count pairs
    counts = {}

    for word in words:
        word = re.sub(r'[,.!%^&*()?:;\'\"\\\/0-9]', '', word) # filter special characters and numbers
        if len(word) > 3: # ignore words with len < 4
            counts[word] = counts.get(word, 0) + 1

    # sort 'counts' dics with words
    counts_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # print spesified count of most common words
    print('  N  | Count | Word')
    try: #verification for case when 'caounts_sorted' would be empty
        for i in range(firstWord,lastWord+1):
            print(i, ' | ', counts_sorted[i][1], ' | ', counts_sorted[i][0])
    except Exception:
        print('File does not contain separate word with len > 3 ')

print(wordsCounting("1.txt",1000,1100))
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




#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# import string
# import sys
#
#
# words = {}
# strip = string.whitespace + string.punctuation + string.digits + "\"'"
# for filename in sys.argv[1:]:
#     for line in open(filename):
#         for word in line.lower().split():
#             word = word.strip(strip)
#                                   if len(word) > 2:
#                 words[word] = words.get(word, 0) + 1
# for word in sorted(words):
#     print("'{0}' occurs {1} times".format(word, words[word]))





#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# import collections
# import string
# import sys
#
#
# words = collections.defaultdict(int)
# strip = string.whitespace + string.punctuation + string.digits + "\"'"
# for filename in sys.argv[1:]:
#     for line in open(filename):
#         for word in line.lower().split():
#             word = word.strip(strip)
#             if len(word) > 2:
#                 words[word] += 1
# for word in sorted(words):
#     print("'{0}' occurs {1} times".format(word, words[word]))

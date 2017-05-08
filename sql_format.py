'''
LICENSE

Copyright (c) 2017, Marufenko Mykhailo
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import sys
import re

def main():
    file = 'tmp1.sql'
    print('\n')            # sys.stdout.write('\n')
    print('File: ' + file) #sys.stdout.write('File: ' + sys.argv[1])
    print('\n')            # sys.stdout.write('\n')

    # create new file
    new_file_name = file[:4] + '_formated.sql'       # new_file_name = sys.argv[1][:4] + '_formated.sql'
    new_file = open(new_file_name, 'w')

    old_file = open(file,'r') # open file for format # old_file = open(sys.argv[1], 'r')

    # parsing
    one_row_query     = one_row(old_file.read())
    upper_case_query  = upper_case(one_row_query)
    indentation_query = indentation(upper_case_query)
    print(one_row_query)
    print(upper_case_query)
    print(indentation_query)

    # new_file.write(indentation_query)

    new_file.close()
    old_file.close()

    print('Done.')                                   # sys.stdout.write('Done.')


def one_row(or_query):
    # function returns query in one row without duplicates of whitespaces
    or_query.replace("\n", " ")                      # drop '\n' symbols
    or_query = ' '.join(or_query.split())            # drop duplicated whitespaces
    return or_query


# def upper_case(uc_query):
#     # function returns query in upper case except quoted parts
#     uc_sub_strings    = []
#     uc_start_position = 0
#     uc_quote          = None
#
#     for i in range(len(uc_query)):
#         if uc_quote is None and uc_query[i] in "\"'":                                      # for substring without quotes
#             uc_end_position   = i
#             uc_sub_strings.append(uc_query[uc_start_position:uc_end_position].upper())
#             uc_start_position = uc_end_position
#             uc_quote          = uc_query[i]
#         elif uc_quote is not None and uc_query[i] == uc_quote:                             # for substring in quotes
#             uc_end_position   = i
#             uc_sub_strings.append(uc_query[uc_start_position:uc_end_position + 1])
#             uc_start_position = uc_end_position + 1
#             uc_quote          = None
#         elif i == len(uc_query) - 1:                                                       # for last char in string
#             uc_sub_strings.append(uc_query[i])
#
#     uc_upper_case_string = ''.join(uc_sub_strings)
#     return uc_upper_case_string


def upper_case(uc_query):
    # function returns query in upper case except quoted parts
    uc_sub_strings = []
    uc_quotes = []
    for i in range(len(uc_query)):
        if len(uc_quotes) % 2 == 0 and uc_query[i] not in "\"'":
            uc_sub_strings.append(uc_query[i].upper())
        elif len(uc_quotes) % 2 == 1 and uc_query[i] not in "\"'":
            uc_sub_strings.append(uc_query[i])
        elif uc_query[i] in "\"'":
            uc_quotes.append(uc_query[i])
            uc_sub_strings.append(uc_query[i])

    uc_upper_case_string = ''.join(uc_sub_strings)
    return(uc_upper_case_string)

def indentation(i_query):
    key_word_dict = {
        "SELECT":   "",
        "FROM":     "\n  ",
        "WHERE":    "\n ",
        "AND":      "   ",
        "GROUP BY": "\n ",
        "HAVING":   "",
        "ORDER BY": "\n "
    }

    # for key in key_word_dict:
    #     if key in i_query:
    #         position = i_query.find(key)
    #         i_query  = i_query[:position] + "\n" + key_word_dict[key] + i_query[position:]

    for key in key_word_dict:
        occurrences = [m.start() for m in re.finditer(key,i_query)]
        for o_position in occurrences:
            i_query = i_query[:o_position] + "\n" + key_word_dict[key] + i_query[o_position:]
            # occurrences = [o + len(key_word_dict[key]) for o in occurrences]

    return i_query


if __name__ == '__main__':
    main()
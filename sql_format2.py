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
    new_file_name = file[:-4] + '_formated.sql'       # new_file_name = sys.argv[1][:4] + '_formated.sql'
    new_file = open(new_file_name, 'w')

    old_file = open(file,'r') # open file for format # old_file = open(sys.argv[1], 'r')

    # parsing
    one_row_query          = one_row(old_file.read())
    upper_case_query       = upper_case(one_row_query)
    indentation_query      = indentation(upper_case_query)

    # comma formating
    final_rows = []
    row_scope = ['SELECT ', 'GROUP BY ', 'ORDER BY ']
    for item in row_scope:
        for row in indentation_query.split('\n'):
            if item in row:
                final_rows.append(comma_format(row))
            else:
                final_rows.append(row + '\n')
        indentation_query = ''.join(final_rows)

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
    # function returns query with aligned indents before each keyword

    key_word_dict = {
        "SELECT":   "  ",
        "FROM":     "\n    ",
        "JOIN":     "    ",
        "WHERE":    "\n   ",
        "GROUP BY": "\n",
        "HAVING":   "  ",
        "ORDER BY": "\n"
    }

    for key in key_word_dict:
        occurrences = [m.start() for m in re.finditer(key,i_query)]
        i = 0
        for o_position in occurrences:
            i_query = i_query[:(o_position + i)] + "\n" + key_word_dict[key] + i_query[(o_position + i):] # after first occurence all following should take into account that str is update with some count of chars
            i += len(key_word_dict[key]) + 1

    return i_query


def spaces_around_commas(sac_query):
    # drop/add spaces where required
    parantheses_list = []
    for i in range(len(sac_query)):
        if sac_query[i] == '(':
            parantheses_list.append(sac_query[i])
        elif parantheses_list and sac_query[i] == parantheses_list[-1]:
            parantheses_list.pop()
        elif sac_query[i] == ',' and not parantheses_list and sac_query[i+1] == ' ':
            sac_query = sac_query[:i+1] + sac_query[i+2:] + ' '
        elif sac_query[i] == ',' and parantheses_list and sac_query[i+1] != ' ':
            sac_query = sac_query[:i+1] + ' ' + sac_query[i+1:]

    return sac_query.rstrip()


def comma_format(cf_query):
    # function put each field separated by comma on separate line

    cf_query = spaces_around_commas(cf_query)

    # block required to take into account only ',' chars outside
    parantheses_list = []
    char_list        = []
    for char in cf_query:
        if char == '(':
            parantheses_list.append(')')
            char_list.append(char)
        elif parantheses_list and char == parantheses_list[-1]:
            parantheses_list.pop()
            char_list.append(char)
        elif char == ',' and not parantheses_list:
            char_list.append('\n' + ',')
        else:
            char_list.append(char)

    cf_query = ''.join(char_list)

    # count length of indent
    indent_len = len(cf_query.split('\n')[0].rstrip().rsplit(' ', 1)[0]) + 1

    # add appropriate indent before each ','
    row_list = []
    i = 0
    for row in cf_query.split('\n'):
        if not i:
            row_list.append(row + '\n')
            i += 1
        else:
            row_list.append(' ' * indent_len + row + '\n')

    cf_query = ''.join(row_list)
    return cf_query


if __name__ == '__main__':
    main()

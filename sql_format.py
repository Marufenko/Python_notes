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
    if ' JOIN ' in indentation_query:
        indentation_query  = alignment_join(indentation_query)
    if ' WHERE ' in indentation_query:
        indentation_query  = alignment_where(indentation_query)
    final                  = alignment_comma(indentation_query)
    print(final)

    # new_file.write(indentation_query)

    new_file.close()
    old_file.close()

    print('Done.')                                   # sys.stdout.write('Done.')


def one_row(or_query):

    # начнем с дополнения пробелами спец символов
    symbol_list = ['=', '>', '<', '/', '^', '+', '-']
    for item in symbol_list:
        or_query = or_query.replace(item, ' ' + item + ' ')

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


def alignment_join(join_query):
    # function returns query With interline formatting

    # теперь строки с join разделим на несколько строк по 'AND'
    a_rows = []
    for row in join_query.split('\n'):
        if (' ON ' in row) and (' AND ' in row):
            # разбиение по ANDам
            for k in range(len(row.split(' AND '))):
                if k < len(row.split(' AND ')) - 1:
                    a_rows.append((row.split(' AND '))[k] + "\n     AND ")
                else:
                    a_rows.append((row.split(' AND '))[k] + "\n")
        else:
            a_rows.append(row + '\n')

    # соберем строчки вместе
    a_query_temp = ''.join(a_rows)

    # посчитаем кол-во знаковперед ON что бы сдвинуть AND в секции JOIN
    on_position = []
    for row in a_query_temp.split('\n'):
        if ' FROM ' in row:
            on_position.append(len(row))
        elif ' ON ' in row:
            on_position.append(len((row.split(' ON '))[0]))
    max_on_value = max(on_position) - 4

    # двигаем ANDы и ON в JOIN секции
    a_row_m = []
    for row in a_query_temp.split('\n'):
        if ' ON ' in row:
            dif = 0
            row_len = len(row.split(' ON ')[0])
            if row_len < max_on_value:
                dif = max_on_value - row_len + 4
            if dif:
                a_row_m.append(row.split(' ON ')[0] + ' '*dif + '  ON ' + row.split(' ON ')[1] + '\n')
            else:
                a_row_m.append(row.replace(' ON ', '  ON ') + '\n')
        elif ' AND ' in row and ' WHERE ' not in row:
            a_row_m.append(' '*max_on_value + row + '\n')
        else:
            a_row_m.append(row + '\n')
    m_query = ''.join(a_row_m)

    # найдем самую длинную строку перед знаком равно
    equal_positions = []
    for row in m_query.split('\n'):
        if ' JOIN ' in row or (' AND ' in row and ' WHERE ' not in row):
            equal_positions.append(len((row.split('='))[0]))
    max_value = max(equal_positions)

    # теперь будем дополнять пробелами секции join игнорирую where
    a_rows_f = []
    for row in m_query.split('\n'):
        if ('=' in row) and (' WHERE ' not in row):
            a_rows_f.append(((row.split('='))[0] + " "*max_value)[:max_value] + '=' + (row.split('='))[1] + '\n')
        else:
            a_rows_f.append(row + '\n')

    join_query = ''.join(a_rows_f)
    return join_query


def alignment_where(where_query):
    # function returns query With interline formatting

    # теперь строки с join разделим на несколько строк по 'AND'
    w_rows = []
    for row in where_query.split('\n'):
        if (' WHERE ' in row) and (' AND ' in row):
            # разбиение по ANDам
            for k in range(len(row.split(' AND '))):
                if k < len(row.split(' AND ')) - 1:
                    w_rows.append((row.split(' AND '))[k] + "\n    wAND ") # нужен специфический символ перед and в секции where что бы отличать от andов в секции join
                else:
                    w_rows.append((row.split(' AND '))[k] + "\n")
        else:
            w_rows.append(row + '\n')

    # соберем строчки вместе
    w_query_temp = ''.join(w_rows)

    # найдем самую длинную строку перед знаком равно
    w_equal_positions = []
    for row in w_query_temp.split('\n'):
        if (' WHERE ' in row) or (' wAND ' in row):
            w_equal_positions.append(len((row.split('='))[0]))
        # else:
        #     pass
    w_max_value = max(w_equal_positions)

    # теперь будем дополнять пробелами секции join игнорирую where
    w_rows_f = []
    for row in w_query_temp.split('\n'):
        if ('=' in row) and (' WHERE ' in row or ' wAND ' in row ):
            w_rows_f.append(((row.split('='))[0] + " "*w_max_value)[:w_max_value] + '=' + (row.split('='))[1] + '\n')
        else:
            w_rows_f.append(row + '\n')

    where_query = ''.join(w_rows_f)

    where_query_final = where_query.replace(' wAND ', '  AND ')

    return where_query_final



def alignment_comma(comma_query):
    # форматирует строки с перечсленными значениями через запятую

    comma_rows = []
    for row in comma_query.split('\n'):
        if ',' in row:
            for i in range(len(row.split(','))):
                if i == 0:
                    comma_rows.append(row.split(',')[0] + '\n')
                else:
                    comma_rows.append(' '*9 + ',' + row.split(',')[i].lstrip() + '\n')
        else:
            comma_rows.append(row + '\n')
    comma_query = ''.join (comma_rows)
    return comma_query


if __name__ == '__main__':
    main()

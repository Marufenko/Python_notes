'''
tool check string b for entry any ocmbination of string s
'''

s = 'acb'
b = 'abaacbbeabca'

result_list = []


pattern_list = [char for char in s]
pattern_list.sort()
print pattern_list

i = 0
while i < len(b) - len(s) + 1:
    tmp_val = b[i:i+len(s)]
    tmp_list = [char for char in tmp_val]
    tmp_list.sort()
    if tmp_list == pattern_list:
        result_list.append(tmp_val)
    i += 1

print result_list



#brootforce
#x='abvcvbabavvbavacacacavvabcabcab'
#a = [x + ": " + str(s.count(x)) for x in list(map("".join, permutations("abc")))]

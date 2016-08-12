s = 'acb'
b = 'abaacbbeabca'

result_list = []

pattern_list = []
for char in s: pattern_list.append(char)
pattern_list.sort()

i = 0
while i < len(b) - len(s) + 1:
    tmp_val = b[i:i+len(s)]
    tmp_list = []
    for char in tmp_val: tmp_list.append(char)
    tmp_list.sort()
    if tmp_list == pattern_list:
        result_list.append(tmp_val)
    i += 1

print result_list

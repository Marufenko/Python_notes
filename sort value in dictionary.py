name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for row in handle:
    if row.startswith('From '):
        row = row.strip()
        tmp_list1 = row.split()
        tmp_list2 = tmp_list1[5].split(':')
        counts[tmp_list2[0]] = counts.get(tmp_list2[0], 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((key,val))
lst.sort()

for val ,key in lst:
    print val, key

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

pairs = {}
for row in handle:
    row = row.strip()
    if row.startswith("From "):
        pairs[row.split()[1]] = pairs.get(row.split()[1], 0) + 1
        
max_v = None
min_k = None
for k,v in pairs.items():
    if max_v is None or v > max_v:
        max_v = v
        max_k = k

print max_k, max_v

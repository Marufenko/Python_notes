name = raw_input("Enter file:")
if len(name) < 1 : name = "1.txt"
handle = open(name)
text = handle.read()
words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

max_v = None
min_k = None
for k,v in counts.items():
    if max_v is None or v > max_v:
        max_v = v
        max_k = k

print max_k, max_v


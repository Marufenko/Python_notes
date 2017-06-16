# 1
numbers = [1,2,3,4,5]
number = [number for number in numbers if number < 4]

# 2
if my_object:
    ... # if my_object is not empty -> True

# 3
if substring in string # check in string

# 4
# print list
a = ['a', 'b', 'c']
print 'Some %s.' %, ', '.join(a)
# it returns "Some a, b, c."

# 5
# create dictionary
d = dict(zip(('id','name','size'),(1948,'W',3)))

# 6
# create inverted dictionary
invented_d = {v:k for k, v in d.items()}

# 7
# create dictionary where key - file name in current folder, value - size in bytes
file_sizes = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.islife(name)}

# 8
# format output
print("'{0}' occurs {1} times".format(word, words[word]))


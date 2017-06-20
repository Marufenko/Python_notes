# for i in 'hello world':
#     if i == 'a':
#         break
# else:
#     print('char a not in string')

a = [1,4,5,78,4,5,5]
for i in a:
    if not str(i).isdigit():
        raise AssertionError('FAIL: str in list')
else:
    print('no str in list')

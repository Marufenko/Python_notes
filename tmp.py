# import time
# start_time = time.time()
#
# input = 1234567890
#
# devision_result = {i+int(input / i):str(i)+','+str(int(input / i)) for i in range(10000,100000) if len(str(int(input / i))) == 5}
#
# max_sum = 0
# for k, v in devision_result.items():
#     if k > max_sum:
#         max_sum = k
#
# print(devision_result[max_sum])
#
# print("--- %s seconds ---" % (time.time() - start_time))

'''
--- 10 // 0.19363665580749512 seconds ---
--- 12 // 2.0804646015167236 seconds ---
--- 14 // 20.2236168384552 seconds ---
--- 16 // MemoryError ---
'''
#
# for i in range(2254786, 2254788):
#         for j in range(5121212, 5121214):
#             print(i, j, i * j)

# 2254786 5121212 11547237120632


import time
start_time = time.time()

float_len = 9

input = 11547237120632

min_val = 0
for k in range(1000000, 10000000):
    if len(str(input / k)) == float_len:
        min_val = (input / k)


devision_result = {i+int(input / i):str(i)+','+str(int(input / i)) for i in range(int(min_val),10000000) if len(str(input / i)) == float_len}

max_sum = 0
for k, v in devision_result.items():
    if k > max_sum:
        max_sum = k

print(devision_result[max_sum])

print("--- %s seconds ---" % (time.time() - start_time))

'''
--- 14 // 31.436270475387573 seconds ---
--- 16 // 330.00336360931396 seconds ---
'''
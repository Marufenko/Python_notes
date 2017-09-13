import numpy
import time
start_time = time.time()

input_value = int(input('Input value: '))
float_len = len(str(input_value)) + 1 # technical variable to verify len of the value

min_val = 0
for k in range(int(10**((len(str(input_value))/2)-1)), int(10**(len(str(input_value))/2))):
    if len(str(int(input_value)/k)) == float_len:
        min_val = (int(input_value)/k)

a_cpu = numpy.arange(int(min_val), int(10**(len(str(input_value))/2)), dtype=numpy.float)
a_calc = input_value/a_cpu + a_cpu

final_pairs = {}
for i in range(len(a_calc)):
    if a_calc[i].is_integer():
        final_pairs[a_calc[i]] = str(a_cpu[i]) + ' & ' + str(input_value/a_cpu[i])

max_sum = 0
for k, v in final_pairs.items():
    if k > max_sum:
        max_sum = k

print(final_pairs[max_sum])

print("--- %s seconds ---" % (time.time() - start_time))

# 3153661524
# 389490263200027000
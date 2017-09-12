'''
https://documen.tician.de/pycuda/tutorial.html#getting-started
create 4x4 array and double each entry
'''

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy

a_gpu = gpuarray.to_gpu(numpy.random.randn(4,4).astype(numpy.float32))
a_doubled = (2*a_gpu).get()

print(a_gpu)
print(a_doubled)
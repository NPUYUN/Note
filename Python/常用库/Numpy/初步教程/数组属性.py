# Numpy 数组属性

import numpy as np

"""
Numpy的数组中比较重要的ndarray对象属性有：

ndarray.ndim：数组的秩。
ndarray.shape：数组的维度，即数组的各个维度大小。
ndarray.size：数组的元素总数。
ndarray.dtype：数组元素的数据类型。
ndarray.itemsize：数组元素的字节大小。
ndarray.flags：包含有关的内存布局信息，如是否为C或Fortran存储，是否为读写，是否为连续的内存块等。
ndarray.real：数组的实部。
ndarray.imag：数组的虚部。
ndarray.data：实际存储数组元素的缓冲区，一般通过索引访问元素，不直接使用该属性。
"""

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

# 实例1：ndarray.ndim
print(a.ndim)
# 可以通过reshape函数调整数组的维度
a.reshape(3, 2)
print(a.ndim)

# 实例2：ndarray.shape
print(a.shape)
# 还可以调整数组大小
a.shape = (2, 3)
print(a)

# 实例3：ndarray.size
print(a.size)

# 实例4：ndarray.dtype
print(a.dtype)

# 实例5：ndarray.itemsize
print(a.itemsize)

# 实例6：ndarray.flags
"""
ndarray.flags 返回 ndarray 对象的内存信息，包含以下属性:
C_CONTIGUOUS (C): 数据是在一个单一的C风格的连续段中
F_CONTIGUOUS (F): 数据是在一个单一的Fortran风格的连续段中
OWNDATA (O): 数组拥有自己的内存或从别的地方借用了内存
WRITEABLE (W): 数组的内容可以被修改，若为 False 则说明内容是只读的
ALIGNED (A): 数组在内存中是按字节对齐到硬件上的
UPDATEIFCOPY (U): 这个数组是其他数组的一个副本，当这个数组被释放时，原数组内容将会被更新
"""
print(a.flags)
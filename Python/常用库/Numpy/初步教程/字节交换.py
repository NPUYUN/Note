# Numpy 字节交换

import numpy as np

"""
在几乎所有机器上，多字节对象都是被存储为连续的字节序列。
字节顺序是跨越多字节的程序对象的存储规则
- 大端模式：最高有效字节在前面，最低有效字节在后面
- 小端模式：最低有效字节在前面，最高有效字节在后面

Numpy提供了将字节进行大小端转换的函数，包括：
numpy.ndarray.byteswap(inplace=False)：字节交换，将字节序列进行大小端转换
- inplace=False：返回一个新的数组，原数组不变
- inplace=True：原数组进行字节交换，原数组变成大小端转换后的数组
默认情况下，inplace=False
"""

# 实例：numpy.ndarray.byteswap(inplace=False)
a = np.array([1, 2, 3, 4] , dtype='i2')
b = a.byteswap()
for i in b:
    print(f"{i:08b}")

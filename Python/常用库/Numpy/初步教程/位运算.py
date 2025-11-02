# Numpy 位运算

import numpy as np

"""
Numpy 提供了一系列位运算函数，允许对数组中的元素进行逐位操作，
这些操作与 Python 的位运算符类似，但作用于 Numpy 数组，支持矢量化处理，性能更高。
Numpy中bitwise_开头的函数是位运算函数，位运算操作包括：

1. numpy.bitwise)and(x1 , x2)：按位与，对应位均为1时，结果为1，否则为0，相当于&运算符。
2. numpy.bitwise_or(x1, x2)：按位或，对应位有一个为1时，结果为1，否则为0，相当于|运算符。
3. numpy.bitwise_xor(x1, x2)：按位异或，对应位不同时为1时，结果为1，否则为0，相当于^运算符。
4. numpy.invert(x)：按位取反，对应位取反，0变1，1变0，相当于~运算符。
5. numpy.left_shift(x1, n)：左移，对应位向左移动n位，低位补0，相当于<<运算符。
6. numpy.right_shift(x1, n)：右移，对应位向右移动n位，低位补0，相当于>>运算符。

在此省略
"""
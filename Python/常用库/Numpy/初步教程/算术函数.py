# Numpy 算术函数

import numpy as np

"""
Numpy提供了一些基本的算术函数，可以对数组进行加减乘除等运算。
在没有特殊说明的情况下，以下函数的参数列表均含有(out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True)，具体含义如下：
- out：输出数组，可选。
- where：布尔数组，指定输出数组中参与计算的元素的位置，可选。
- casting：数组类型转换的规则，可选。
- order：输出数组的内存布局，可选。
- dtype：输出数组的数据类型，可选。
- subok：默认返回一个与输入数组相同类型的数组，如果为True，则返回一个子类数组。
下列函数中，...表示省略该参数列表

1. 基本算术运算函数
需要注意的是，这些函数的输入数组必须相匹配(维度相同，元素个数相同或者为1(触发广播))，否则会报错。
(1) numpy.add(x1, x2, ...)：两个数组相加，返回结果数组。
- x1, x2：两个数组。

(2) numpy.subtract(x1, x2, ...)：两个数组相减(x1-x2)，返回结果数组。
- x1, x2：两个数组。

(3) numpy.multiply(x1, x2, ...)：两个数组相乘，返回结果数组。
- x1, x2：两个数组。

(4) numpy.divide(x1, x2, ...)：两个数组相除(x1/x2)，返回结果数组。
- x1, x2：两个数组。

(5) numpy.floor_divide(x1, x2, ...)：两个数组向下取整除(x1//x2)，返回结果数组。
- x1, x2：两个数组。

(6) numpy.mod(x1, x2, ...)：两个数组取模(x1%x2)，返回结果数组。
- x1, x2：两个数组。

(7) numpy.abs(x, ...)：数组的绝对值，返回结果数组。
- x：数组。

2. 特殊运算函数
(1) numpy.power(x1, x2, ...)：两个数组的幂运算(x1**x2)，返回结果数组。
- x1, x2：两个数组。

(2) numpy.sqrt(x, ...)：数组的平方根，返回结果数组。
- x：数组。

(3) numpy.sign(x, ...)：数组的符号函数(-1 , 0 , 1)，返回结果数组。
- x：数组。

(4) numpy.reciprocal(x, ...)：数组的倒数，返回结果数组。
- x：数组，元素不能为0。

(5) numpy.clip(a, a_min, a_max, ...)：数组的裁剪函数，将数组中的元素限制在a_min和a_max之间，返回结果数组。
- a：数组。
- a_min：最小值。
- a_max：最大值。
注意：元素总数不变，大于a_max的元素被设为a_max，小于a_min的元素被设为a_min。
"""

# 实例1：加减乘除
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# 加法
print(np.add(a, b))
# 减法
print(np.subtract(a, b))
# 乘法
print(np.multiply(a, b))
# 除法
print(np.divide(a, b))
# 向下取整除
print(np.floor_divide(a, b))

# 实例2：取模
a = np.array([10, 20, 30])
b = np.array([3, 4, 5])
print(np.mod(a, b))

# 实例3：绝对值
a = np.array([-1, 0, 1])
print(np.abs(a))

# 实例4：幂运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.power(a, b))

# 实例5：平方根
a = np.array([1, 4, 9])
print(np.sqrt(a))

# 实例6：符号函数
a = np.array([-1, 0, 1])
print(np.sign(a))

# 实例7：倒数
a = np.array([1, 2, 3])
print(np.reciprocal(a)) # 若全为整数，则返回整数部分数组
b = np.array([2, 3.0, 4])
print(np.reciprocal(b)) # 若有浮点数，则返回浮点数数组

# 实例8：裁剪函数
a = np.array([1, 2, 3, 4, 5])
print(np.clip(a, 1, 4))
# Numpy 排序与条件筛选函数

import numpy as np

"""
1. 排序函数
(1) np.sort(a , axis=None, kind='quicksort', order=None, stable=True)
返回数组的排序版本，默认是升序
- a : 输入数组
- axis : 整数，指定排序轴，None表示沿所有轴排序
- kind : 字符串，排序算法，'quicksort'为快速排序，'mergesort'为归并排序，'heapsort'为堆排序
- order : 字符串或元组，指定排序顺序，'C'为按C语言顺序排序，'F'为按Fortran语言顺序排序，元组表示多种排序方式
- stable : 布尔值，指定是否进行稳定排序，True为稳定排序，False为不稳定排序

(2) numpy.argsort(a, axis=-1, kind='quicksort', order=None, stable=True)
返回数组中元素的排序索引，默认是升序
- a : 输入数组
- axis : 整数，指定排序轴，-1表示沿最后一个轴排序
- kind : 字符串，排序算法，'quicksort'为快速排序，'mergesort'为归并排序，'heapsort'为堆排序
- order : 字符串或元组，指定排序顺序，'C'为按C语言顺序排序，'F'为按Fortran语言顺序排序，元组表示多种排序方式
- stable : 布尔值，指定是否进行稳定排序，True为稳定排序，False为不稳定排序

(3) numpy.lexsort(keys, axis=-1)
返回数组中元素的排序索引，根据多个关键字进行排序
- keys : 输入数组，每个元素为一个排序关键字，为字节数组
- axis : 整数，指定排序轴，-1表示沿最后一个轴排序

(4) numpy.sort_complex(a)
返回复数数组的排序版本，对复数按照先实部后虚部的顺序进行排序。
- a : 输入数组

(5) numpy.partition(a, kth, axis=-1, kind='introselect', order=None)
返回数组的分区副本，使第kth位置的元素为排序后的值，左侧的元素都小于等于该值，右侧的元素都大于等于该值
- a : 输入数组
- kth : 整数，指定分区位置
- axis : 整数，指定排序轴，-1表示沿最后一个轴排序
- kind : 字符串，排序算法，'introselect'为快速选择算法，'quicksort'为快速排序，'mergesort'为归并排序，'heapsort'为堆排序
- order : 字符串或元组，指定排序顺序，'C'为按C语言顺序排序，'F'为按Fortran语言顺序排序，元组表示多种排序方式

(6) numpy.argpartition(a, kth, axis=-1, kind='introselect', order=None)
返回数组中元素的分区索引，使第kth位置的元素为排序后的值，左侧的元素都小于等于该值，右侧的元素都大于等于该值
- a : 输入数组
- kth : 整数，指定分区位置
- axis : 整数，指定排序轴，-1表示沿最后一个轴排序
- kind : 字符串，排序算法，'introselect'为快速选择算法，'quicksort'为快速排序，'mergesort'为归并排序，'heapsort'为堆排序
- order : 字符串或元组，指定排序顺序，'C'为按C语言顺序排序，'F'为按Fortran语言顺序排序，元组表示多种排序方式


2. 条件筛选函数
(1) numpy.where(condition, x=None, y=None)
返回满足条件的元素的索引
- condition : 布尔数组，指定条件
- x : 与condition广播兼容的数组，满足条件的元素将替换为x
- y : 与condition广播兼容的数组，不满足条件的元素将替换为y
注意：
如果x和y都为None，则返回满足条件的元素的索引，以元组形式返回，每个维度一个索引数组
若提供x,y：返回与condition形状相同的数组，满足条件的元素将替换为x，不满足条件的元素将替换为y

(2) numpy.extract(condition, arr)
返回满足条件的元素组成的新数组
- condition : 布尔数组，指定条件，与arr的shape相同
- arr : 输入数组，元素满足条件的元素将被提取出来组成新数组

(3) numpy.choose(a, choices, out=None, mode='raise')
根据索引数组a从多个备选数组中选择元素，返回选择结果
- a : 整数数组，索引数组，每个元素对应choices中的一个备选数组
- choices : 数组序列，备选数组序列(列表或元组)，形状与a相同
- out : 输出数组，可选，用于存储选择结果
- mode : 处理越界索引的方式，'raise'为默认，'wrap'位取模，'clip'为截断
注：
索引逻辑：a每个位置的元素对应choices[a]中的相应位置的元素，如果a越界，则根据mode处理

(4) numpy.nonzero(a)
返回非零元素的索引，为元组形式，包含各维度的索引数组
- a : 输入数组

(5) numpy.argwhere(a)
返回非零元素的索引，为二维数组形式，每行为一个坐标
- a : 输入数组

(6) numpy.argmin(a, axis=None, out=None, keepdims=False)
返回数组中最小值的索引
- a : 输入数组
- axis : 整数，指定轴，None表示沿所有轴计算
- out : 输出数组，可选，用于存储结果
- keepdims : 布尔值，是否保持轴的维度，False表示不保持

(7) numpy.argmax(a, axis=None, out=None, keepdims=False)
返回数组中最大值的索引
- a : 输入数组
- axis : 整数，指定轴，None表示沿所有轴计算
- out : 输出数组，可选，用于存储结果
- keepdims : 布尔值，是否保持轴的维度，False表示不保持
"""

# 实例1：排序函数
a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
dt = np.dtype([('name', 'S10'), ('age', int)])
b = np.array([('Alice', 25), ('Bob', 30), ('Charlie', 20), ('David', 25)], dtype=dt)
c = np.array([[1, 3, 2, 4] , [5, 2, 1, 3] , [4, 1, 5, 2]])
d = np.array([1+2j, 2+1j, 3+4j, 4+3j] , dtype=np.complex128)

print(np.sort(a))
print(np.sort(b , order='age')) # 按age排序
print(np.sort(c))
print(np.sort(c , axis=0))

print(np.argsort(a)) # 返回索引
print(np.lexsort((b['age'], b['name']))) # 按照先age后name排序
print(np.sort_complex(d)) # 排序复数

print(np.partition(a, 5)) # 按5分区
print(np.argpartition(a, 5)) # 按5分区，返回索引


# 实例2：条件筛选函数
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0 , 10])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(np.where(a > 5)) # 返回索引
print(np.where(a > 5, a, 0)) # 筛选大于5的元素，不满足的替换为0

print(np.extract(a > 5, a)) # 筛选大于5的元素，组成新数组

print(np.choose([2, 3, 1, 0], choices=[6, 7, 8, 9, 10]))
print(np.choose([2, 4, 1, 10], choices=[6, 7, 8, 9, 10] ,mode='clip')) # 截断处理(直接取最后一个元素)
print(np.choose([2, 4, 1, 10], choices=[6, 7, 8, 9, 10] ,mode='wrap')) # 取模处理(对长度取模)
x = np.array([[0 , 1] , [1 , 1]])
choices = [np.array([[1, 2], [4 , 3]]), np.array([[4, 5] ,[7, 6]])]
print(np.choose(x, choices))

print(np.nonzero(a)) # 返回非零元素的索引
print(np.argwhere(a)) # 返回非零元素的索引
print(np.argmin(a)) # 返回最小值的索引
print(np.argmax(a)) # 返回最大值的索引
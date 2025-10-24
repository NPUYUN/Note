# Numpy核心：N维数组对象(ndarray)
"""
用处：存放同类型的多维数组
内部由以下内容构成：
- 一个指向数据的指针
- 数据类型或者dtype，描述在数组中固定大小值的格子
- 一个表示数组形状的元组，表示各维度大小
- 一个跨度元组，即前进到当前维度的下一元素需要跨过的字节数
"""

import numpy as np

"""
创建一个ndarray：array函数
numpy.array(object, dtype = None, copy = True, order = None , subok = False, ndmin = 0)
参数说明：
- object: 数组或嵌套的数列
- dtype: 数据元素的数据类型，可选
- copy: 对象是否需要复制，可选
- order: 创建数组的样式，C为行优先，F为列优先，A为任意，可选
- subok: 默认返回一个与基类类型一致的数组，可选
- ndmin: 指定生成数组的最小维度，可选
"""

# 实例1：创建1维数组
a = np.array([1 , 2 , 3])
print(a)

# 实例2：创建2维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# 实例3：设置最小维度
c = np.array([1 , 2 , 3] , ndmin = 2)
print(c)

# 实例4：设置数据类型
d = np.array([1 , 2 , 3] , dtype = complex)
print(d)

"""
小结：
ndarray 对象由计算机内存的连续一维部分组成，并结合索引模式，将每个元素映射到内存块中的一个位置。
内存块以行顺序(C样式)或列顺序(FORTRAN或MatLab风格，即前述的F样式)来保存元素。
"""
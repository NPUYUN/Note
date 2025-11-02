# Numpy 数组操作

import numpy as np

"""
Numpy中包含了一些函数用于处理数组，大概可分为以下几类：
修改数组形状
(1) numpy.reshape(array, newshape, order='C')：在不改变数据的条件下修改形状
- array：待修改的数组
- newshape：目标形状，为整数或者整数数组，兼容原有形状
- order：'C'表示按行优先，'F'表示按列优先，'A'表示保持原有顺序，'k'表示元素在内存中出现的顺序
补充：numpy.ndarray.shape(newshape)：修改数组形状，返回修改后的数组

(2) numpy.ndarray.flat：数组元素迭代器

(3) numpy.ndarray.flatten(order='C')：返回一份数组拷贝，不会改变原数组，会将数组展开成一维数组
- order：'C'表示按行优先，'F'表示按列优先，'A'表示保持原有顺序，'k'表示元素在内存中出现的顺序

(4) numpy.ravel(array, order='C')：返回一份数组拷贝，不会改变原数组
- array：待修改的数组
- order：'C'表示按行优先，'F'表示按列优先，'A'表示保持原有顺序，'k'表示元素在内存中出现的顺序
"""

# 实例1：numpy.reshape(array, newshape, order='C')
a = np.arange(6)
print(a.reshape([2,3])) # 采用ndarray.reshape()方法
np.reshape(a , [3,2]) # 采用numpy.reshape()函数
print(a)

# 实例2：numpy.ndarray.flat
a = np.arange(6).reshape([2,3])
for i in a.flat:
    print(i , end=' ')
print()

# 实例3：numpy.ndarray.flatten(order='C')
a = np.arange(6).reshape([2,3])
print(a.flatten())
# 按列优先
print(a.flatten('F'))

# 实例4：numpy.ravel(array, order='C')
a = np.arange(6).reshape([2,3])
print(np.ravel(a))
# 按列优先
print(np.ravel(a, 'F'))


"""
翻转数组
(1) numpy.transpose(array , axes=None)：对换数组的维度
- array：待修改的数组
- axes：整数列表，对应维度，通常为None，表示全部维度交换
补充：numpy.ndarray.T：对换数组的维度，等同于numpy.transpose(array)

(2) numpy.rollaxis(array, axis , start=0)：向后滚动特定轴到一个特定的位置
- array：待修改的数组
- axis：要向后滚动的轴，其他的轴的相对位置不会改变
- start：滚动的位置，默认为0，表示完整的滚动

(3) numpy.swapaxes(array, axis1, axis2)：交换数组的两个轴
- array：待修改的数组
- axis1：第一个轴
- axis2：第二个轴
"""

# 实例1：numpy.transpose(array , axes=None)
a = np.arange(6).reshape([2,3])
print(a)
print(np.transpose(a))
print(a.T)


# 实例2：numpy.rollaxis(array, axis , start=0)
a = np.arange(8).reshape([2,2,2])
print(np.where(a==1)) # 找出数组中值为1的元素的索引
b = np.rollaxis(a , 2 , 0) # 轴2向前滚动到轴0
print(np.where(b==1))
c = np.rollaxis(b , 2 , 0) # 轴0向后滚动到轴2
print(np.where(c==1))

# 实例3：numpy.swapaxes(array, axis1, axis2)
a = np.arange(6).reshape([2,3])
print(a)
print(np.swapaxes(a,0,1)) # 交换轴0和轴1


"""
修改数组维度
(1) numpy.broadcast(array1, array2)：模仿广播的对象，返回封装了将一个数组广播到另一个数组的结果的对象
- array1：待广播的数组
- array2：目标数组
注意：该对象拥有iterator属性，基于自身组件的迭代器元组，同python的迭代器一致：
变量1，变量2... = broadcast对象.iters：取出迭代器元组
next(变量1)，next(变量2)...：取出迭代器的下一个元素

(2) numpy.broadcast_to(array, shape, subok=False)：将数组广播到指定形状
- array：待广播的数组
- shape：目标形状，为整数或者整数数组，需要符合广播规则
- subok：默认为False，表示返回的数组为子类，否则为ndarray

(3) numpy.expand_dims(array, axis)：在指定轴上增加新的维度
- array：待修改的数组
- axis：整数，新轴插入的位置，负数表示倒数第几个轴

(4) numpy.squeeze(array, axis)：删除一维的条目
- array：待修改的数组
- axis：整数或整数列表，要删除的轴，默认为空，表示删除所有长度为1的轴
"""
# 实例1：numpy.broadcast(array1, array2)
a = np.array([[1],[2],[3]])
b = np.array([4,5,6])
c = np.broadcast(a,b)
print(c)
r,t = c.iters
print(next(r) , next(t))
print(next(r) , next(t))
k = np.broadcast(a,b)
print(k.shape)
d = np.empty(k.shape)
d.flat = [u + v for (u,v) in k] # 元组表达式求a + b的具体值
print(d)

# 实例2：numpy.broadcast_to(array, shape, subok=False)
a = np.arange(4).reshape([1,4])
print(a)
print(np.broadcast_to(a , [4,4]))

# 实例3：numpy.expand_dims(array, axis)
a = np.array([[1,2] , [3,4]])
b = np.expand_dims(a, axis=2)
print(b.shape)

# 实例4：numpy.squeeze(array, axis)
a = np.arange(9).reshape((1 , 3, 3))
b = np.squeeze(a)
print(b)
print(b.shape)


"""
连接数组
(1) numpy.concatenate((array1, array2,...),axis)：沿指定轴连接相同形状的两个或者多个数组
- array1，array2...：待连接的相同类型的数组
- axis：沿着它连接数组的轴，默认为0

(2) numpy.stack((array1,array2,...),axis)：沿着新轴连接数组序列
- array1，array2...：待连接的数组序列
- axis：返回数组中的值，输入数组沿着它来堆叠 
与concatenate()的区别：concatenate()沿着指定轴连接数组，而stack()沿着新轴连接数组序列

(3) numpy.hstack((array1, array2,...))：沿着水平方向连接数组
- array1，array2...：待连接的数组

(4) numpy.vstack((array1, array2,...))：沿着垂直方向连接数组
- array1，array2...：待连接的数组

注意：hstack()和vstack()都是将数组沿着指定轴连接，与stack不同而与concatenate()相同
"""

# 实例1：numpy.concatenate((array1, array2,...),axis)
a = np.array([[1,2] , [3,4]])
b = np.array([[5,6] , [7,8]])
c = np.concatenate((a,b),axis=1)
print(c)

# 实例2：numpy.stack((array1,array2,...),axis)
a = np.array([[1,2] , [3,4]])
b = np.array([[5,6] , [7,8]])
c = np.stack((a,b),axis=1)
print(c)

# 实例3：numpy.hstack((array1, array2,...))
a = np.array([[1,2] , [3,4]])
b = np.array([[5,6] , [7,8]])
c = np.hstack((a,b))
print(c)

# 实例4：numpy.vstack((array1, array2,...))
a = np.array([[1,2] , [3,4]])
b = np.array([[5,6] , [7,8]])
c = np.vstack((a,b))
print(c)


"""
分割数组
(1) numpy.split(array, indices_or_sections, axis=0)：分割数组
- array：待分割的数组
- indices_or_sections：如果为整数，就用该数平均切分；如果是一个数组，为沿轴切分的位置(左开右闭)
- axis：沿着它分割数组的轴，默认为0，横向切分

(2) numpy.hsplit(array, indices_or_sections)：沿水平轴分割数组
- array：待分割的数组
- indices_or_sections：如果为整数，就用该数平均切分；如果是一个数组，为沿轴切分的位置(左开右闭)

(3) numpy.vsplit(array, indices_or_sections)：沿垂直轴分割数组
- array：待分割的数组
- indices_or_sections：如果为整数，就用该数平均切分；如果是一个数组，为沿轴切分的位置(左开右闭)
"""

# 实例1：numpy.split(array, indices_or_sections, axis=0)`
a = np.arange(9).reshape((3,3))
b = np.split(a, 3 , axis=0) # 分成三个大小相等的子数组
print(b)
c = np.split(a , [3 , 4] , axis=1) # 分成两个子数组
print(c)

# 实例2：numpy.hsplit(array, indices_or_sections)
a = np.arange(9).reshape((3,3))
b = np.hsplit(a, 3) # 水平方向分割成三个子数组
print(b)

# 实例3：numpy.vsplit(array, indices_or_sections)
a = np.arange(9).reshape((3,3))
b = np.vsplit(a, 3) # 垂直方向分割三两个子数组
print(b)


"""
数组元素的添加和删除
(1) numpy.resize(array，new_shape)：返回指定大小的新数组，如果新数组大小大于原始大小，则包含原始数组中的元素的副本，即重复出现
- array：待修改的数组
- new_shape：目标形状，为整数或者整数数组，兼容原有形状

(2) numpy.append(array, values, axis=None)：在指定轴上添加元素
- array：待修改的数组
- values：待添加的元素
- axis：整数，指定轴，默认为None，表示在末尾添加元素且返回一维数组

(3) numpy.insert(array, obj, values, axis=None)：在指定轴上插入元素
- array：待修改的数组
- obj：整数或整数数组，指定插入位置
- values：待插入的元素
- axis：整数，指定轴，如果未提供则数组会被展开
若在指定轴上添加一个元素，则会触发广播机制，即将元素广播到整个数组

(4) numpy.delete(array, obj, axis=None)：删除指定轴上的元素
- array：待修改的数组
- obj：整数或整数数组，指定删除位置，可以被切片，表明要从输入数组删除的子数组
- axis：整数，指定轴，如果未提供则数组会被展开

(5) numpy.unique(array, return_index=False, return_inverse=False, return_counts=False)：去除数组中的重复元素，并返回索引、逆索引、计数
- array：待修改的数组，如果不是一维数组，则会展开
- return_index：是否返回新列表元素在旧列表中的位置(下标)，并以列表的形式存储，默认为False
- return_inverse：是否返回旧列表元素在新列表中的位置(下标)，并以列表的形式存储，默认为False
- return_counts：是否返回去重数组中的元素在原数组的出现次数，默认为False
"""

# 实例1：numpy.resize(array，new_shape)
a = np.arange(6).reshape([2,3])
b = np.resize(a, [3,2])
print(b)
c = np.resize(a , [2 , 6])
print(c)

# 实例2：numpy.append(array, values, axis=None)
a = np.arange(6).reshape([2,3])
b = np.append(a, [7,8,9]) # 在末尾添加元素，没有指定轴，返回一维数组
print(b)
c = np.append(a, [[7,8,9]] , axis=0) # 在指定轴上添加元素，返回二维数组
print(c)

# 实例3：numpy.insert(array, obj, values, axis=None)
a = np.arange(6).reshape([2,3])
b = np.insert(a, 1, 1) # 在指定位置插入元素，没有指定轴，返回一维数组
print(b)
c = np.insert(a, 1, [1,2] , axis=1) # 在指定位置插入元素，指定了轴为1，返回二维数组
print(c)
d = np.insert(a , 1 , 1 , axis=1) # 在指定位置插入元素，指定了轴为0，返回二维数字，且元素广播到整个数组
print(d)

# 实例4：numpy.delete(array, obj, axis=None)
a = np.arange(6).reshape([2,3])
b = np.delete(a, 1,) # 删除指定位置的元素，没有指定轴，返回一维数组
print(b)
c = np.delete(a, 1, axis=1) # 删除指定轴上的元素，返回二维数组
print(c)
d = np.delete(a , np.s_[::2]) # 通过切片删除元素
print(d)

# 实例5：numpy.unique(array, return_index=False, return_inverse=False, return_counts=False)
a = np.array([1,2,3,2,1,4,5,4,6,7,6,5,4,3,2,1])
b = np.unique(a) # 去除重复元素，返回一维数组
print(b)
c,indices = np.unique(a, return_index=True) # 去除重复元素，返回一维数组和新数组在旧数组中的索引
print(c)
print(indices)
d,inverse = np.unique(a, return_inverse=True) # 去除重复元素，返回一维数组以及旧数组在新数组中的索引
print(d)
print(inverse)
print(c[inverse]) # 按索引顺序重排c
e,counts = np.unique(a, return_counts=True) # 去除重复元素，返回一维数组以及每个元素在原数组中出现的次数
print(e)
print(counts)
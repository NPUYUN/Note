# Numpy 创建数组

import numpy as np

"""
ndarray数组除了可以使用底层的ndarray构造器来创建外，也可以使用以下几种一般方式来创建数组：
1. numpy.empty(shape, dtype=float, order='C')
创建一个指定形状、数据类型且未初始化的数组。
- shape：数组形状，可以为列表、元组以及整数(表示创建一维数组)
- dtype：数据类型，默认为float，可选
- order：内存布局，默认为C，支持‘C’(行优先)、‘F’(列优先)、‘A’(任意)三种布局。

2. numpy.zeros(shape, dtype=float, order='C')
创建一个指定形状、数据类型且元素均为0的数组。
- shape：数组形状，可以为列表、元组以及整数(表示创建一维数组)
- dtype：数据类型，默认为float，可选
- order：内存布局，默认为C，支持‘C’(行优先)、‘F’(列优先)、‘A’(任意)三种布局。

3. numpy.ones(shape, dtype=float, order='C')
创建一个指定形状、数据类型且元素均为1的数组。
- shape：数组形状，可以为列表、元组以及整数(表示创建一维数组)
- dtype：数据类型，默认为float，可选
- order：内存布局，默认为C，支持‘C’(行优先)、‘F’(列优先)、‘A’(任意)三种布局。

4. numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)
创建一个与另一个数组a相同形状、数据类型且元素均为0的数组。
- a：给定的要创建相同形状的数组
- dtype：创建数组的数据类型，默认为None，即与a相同
- order：数组在内存中的存储顺序，默认为K，即与a相同
- subok：是否允许返回子类，默认为True，即返回一个与a相同的子类数组，否则返回一个与a数组具有相同数据类型和存储顺序的数组
- shape：创建数组的形状，默认为None，即与a相同

5. numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)
创建一个与另一个数组a相同形状、数据类型且元素均为1的数组。
- a：给定的要创建相同形状的数组
- dtype：创建数组的数据类型，默认为None，即与a相同
- order：数组在内存中的存储顺序，默认为K，即与a相同
- subok：是否允许返回子类，默认为True，即返回一个与a相同的子类数组，否则返回一个与a数组具有相同数据类型和存储顺序的数组
- shape：创建数组的形状，默认为None，即与a相同
"""

# 实例1：numpy.empty(shape, dtype=float, order='C')
a = np.empty([1 , 2] , dtype = int)
print(a)

# 实例2：numpy.zeros(shape, dtype=float, order='C')
# 默认为浮点数
a = np.zeros(5)
print(a)
# 设置类型为整数
a = np.zeros(5, dtype=int)
print(a)
# 自定义结构化数组类型
b = np.zeros((2 , 2) , dtype = [('x' , 'i4') , ('y' , 'f4')])
print(b)

# 实例3：numpy.ones(shape, dtype=float, order='C')
# 默认为浮点数
a = np.ones(5)
print(a)
# 自定义类型
b = np.ones((2 , 2) , dtype = int)

# 实例4：numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)
arr = np.array([[1, 2, 3], [4, 5, 6]])
a = np.zeros_like(arr)
print(a)

# 实例5：numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)
arr = np.array([[1, 2, 3], [4, 5, 6]])
a = np.ones_like(arr)
print(a)



"""
ndarray数组可以从已有的数组中创建，有以下几种方式：
1. numpy.asarray(a, dtype=None, order=None)
类似于numpy.array()，但可以将其他数组转换为ndarray。但是只有三个参数，且为直接使用已有数组的内存，不进行复制。
- a：任意形式的输入参数，可以是列表、列表的元组、元组、元组的元组、元组的列表、N维数组(ndarray)等
- dtype：数据类型，可选
- order：内存布局，可选
当数据源不为ndarray时，与numpy.array()相同。
当数据源为ndarray时，numpy.asarray()直接返回引用，不复制数据，会导致修改原数组。

2. numpy.frombuffer(buffer, dtype=float, count=-1, offset=0)
实现动态数组，接受buffer传入参数，以流的形式读入转化为ndarray对象
注意：buffer是字符串时，python3默认str为Unicode类型，所以要转成bytestring，在原str前加上b
- buffer：可以是任意对象，会以流的形式读入
- dtype：返回数组的数据类型，可选
- count：读取的元素个数，默认为-1，即读取全部
- offset：读取的起始位置，默认为0

3. numpy.fromiter(iterable, dtype, count=-1)
从可迭代对象创建ndarray对象，返回一维数组
- iterable：可迭代对象
- dtype：返回数组的数据类型
- count：读取的元素个数，默认为-1，即读取全部
"""

# 实例1：numpy.asarray(a, dtype=None, order=None)
# 将列表转换为ndarray
x = [1, 2, 3]
a = np.asarray(x)
print(a)
# 将元组转换为ndarray
x = (1, 2, 3)
a = np.asarray(x)
print(a)
# 将元组列表转换为ndarray
x = [(1 , 2,  3) , (4 , 5 , 6)]
a = np.asarray(x)
print(a)
# 设置了dtype参数
x = [1, 2, 3]
a = np.asarray(x , dtype = float)
print(a)

# 实例2：numpy.frombuffer(buffer, dtype=float, count=-1, offset=0)
s = b'1234567890' # 字符串转成bytestring
a = np.frombuffer(s , dtype = 'S1')
print(a)

# 实例3：numpy.fromiter(iterable, dtype, count=-1)
list = range(10)
it = iter(list)
a = np.fromiter(it , dtype = float)
print(a)


"""
此外，Numpy还可以从数值范围创建数组，有以下几种方式：
1. numpy.arange(start=0, stop, step=1, dtype=None)
根据start和stop指定的范围以及step指定的步长，生成一个ndarray对象。
- start：起始值，默认为0
- stop：终止值(不包含)
- step：步长，默认为1
- dtype：数据类型，可选，默认为输入数据的类型

2. numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
创建一个一维数组，数组是一个等差数列。
- start：序列的起始值
- end：序列的终止值，如果endpoint为True，则包含终止值
- num：要生成的等步长的样本数量，默认为50
- endpoint：是否包含终止值，默认为True
- retstep：是否返回步长，默认为False
- dtype：数据类型，可选，默认为输入数据的类型
即将start和stop之间的数等分成num个，步长恒定，返回一个等差数列。

3. numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
创建一个一维数组，数组是一个对数等比数列。
- start：序列的起始值为base**start
- end：序列的终止值为base**stop，如果endpoint为True，则包含终止值
- num：要生成的等步长的样本数量，默认为50
- endpoint：是否包含终止值，默认为True
- base：对数log的底数，默认为10.0
- dtype：数据类型，可选，默认为输入数据的类型
即将base**start和base**end之间的数分成num个，前后数字在取base为底的对数后为等差数列
也就是说，logspace实际上创建的是以base为底的对数的等差数列。即先生成start和stop的等差数列，然后再取base为底数的指数。
如：start=1,stop=2,num=11,那么生成的数组取以base为底的对数后为[1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
"""

# 实例1：numpy.arange(start, stop, step=1, dtype=None)
# 生成0到4长度为5的数组
a = np.arange(5)
print(a)
# 设置返回类型为float
a = np.arange(5, dtype=float)
print(a)
# 设置起始值、终止值、步长
a = np.arange(1 , 5 , 2)
print(a)

# 实例2：numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
a = np.linspace(1 , 10 , 10)
print(a)
#设置全部元素为1的等差数列
a = np.linspace(1 , 1 , 10)
print(a)
# 不包含stop值的等差数列
a = np.linspace(1 , 10 , 10 , endpoint=False)
print(a)
# 返回步长：步长默认为float
a = np.linspace(1 , 10 , 10 , retstep=True)
print(a)

# 实例3：numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# 默认底数为10
a = np.logspace(1.0, 2.0 , num = 11)
print(a)
# 设置底数为2
a = np.logspace(0, 9 , 10 , base = 2)
print(a)
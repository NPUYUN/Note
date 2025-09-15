#本文件为学习Numpy的笔记

#1.Ndarray对象
print("===========================================")
import numpy as np #导入numpy库

'''
基本语法：
numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
numpy:表示numpy库的别名/模块。
object：数组或嵌套的数列，可以是列表、元组、元组列表等。
dtype：数组元素的数据类型，默认为None，表示由输入对象推断。
copy：布尔值，默认为True，表示是否复制输入对象。
order：内存布局，默认为'K'，表示保持输入数组的内存布局。
subok：布尔值，默认为False，表示返回的数组是否为子类。
ndmin：指定生成数组的最小维度，默认为0。
'''

#实例1:创建1维数组
a = np.array([1 , 2 , 3 , 4 , 5])
print(a)

#实例2:创建2维数组
b = np.array([[1 , 2 , 3] , [4 , 5 , 6]])
print(b)

#实例3:最小维度
c = np.array([1 , 2 , 3] , ndmin = 2)
print(c)

#实例4:数据类型
d = np.array([1 , 2 , 3] , dtype = complex)
print(d)


#2.Numpy中的数据类型
#常用NumPy数据类型：
#int8, int16, int32, int64, uint8, uint16, uint32, uint64, float16, float32, float64, complex64, complex128

#数据类型对象:dtype
'''
基本语法：
numpy.dtype(object, align=False, copy=False)
object：数据类型对象，可以是字符串、数据类型对象、字典等。
align：布尔值，默认为False，表示是否对齐数据。
copy：布尔值，默认为False，表示是否复制数据。
'''
print("===========================================")

#实例1:使用标量类型
dt = np.dtype(np.int32)
print(dt)

#实例2:不同的相同类型(int8(i1), int16(i2), int32(i4), int64(i8)，其余类似)
dt = np.dtype('i4')
print(dt)

#实例3:按字节顺序标注(<表示小端(最小地址在前面)，>表示大端（最小地址在后面))
dt = np.dtype('<i4')
print(dt)

#实例4:创建结构化数据类型
dt = np.dtype([('age' , np.int8)]) #age字段为int8类型
print(dt)

#实例5:将数据类型应用于ndarray
a = np.array([(10,) , (20 ,) , (30 , )] , dtype = dt) #元组只有一个元素，所以需要加逗号
print(a)

#实例6:类型的字段名可以用于存储实际的数据
print(a['age'])

#实例7:结构化数据类型可以包含多种类型字段
student = np.dtype([('name' , 'S20') , ('age' , 'i4') , ('markd', 'f4')])
print(student)

a = np.array([('abc' , 21 , 50) , ('xyz' , 18 , 75)])
print(a)

'''
内建类型：
b：布尔类型，True或False
i：整数类型,如i1、i2、i4、i8
u：无符号整数类型,如u1、u2、u4、u8
f：浮点数类型,如f2、f4、f8
c：复数类型，由实部和虚部构成,如c8、c16
m：timedelta类型，时间间隔,如m8、m16、m32、m64
M：datetime类型，日期时间,如M8、M16、M32、M64
O：对象类型，Python对象,如O0、O1、O2、O4、O8、O16、O32、O64
S：字符串类型，固定长度的字节序列,如S5、S10、S20、S30、S40、S50、S60、S70、S80、S90、S100
U：Unicode字符串类型，固定长度的Unicode序列,如U5、U10、U20、U30、U40、U50、U60、U70、U80、U90、U100
V：原始数据类型，原始数据缓冲区,如V0、V1、V2、V4、V8、V16、V32、V64、V128、V256
'''


#3.Numpy数组的属性
'''
ndarray.ndim：数组的秩，即数组的维数。
ndarray.shape：数组的维度，即数组的各维度大小，如对于二维数组，shape=(2,3)表示有2行3列。
ndarray.size：数组的元素总数，等于ndarray.shape中各维度元素的乘积。
ndarray.dtype：数组元素的数据类型。
ndarray.itemsize：数组元素的字节大小。
ndarray.flags：数组的内存信息.
ndarray.real: 数组的实部。
ndarray.imag: 数组的虚部。
ndarray.data：实际存储数组元素的缓冲区，可以通过ctypes模块将缓冲区转换为Python对象。不直接使用该属性。
'''
print("===========================================")

#实例1:ndarray.ndim
a = np.array([1 , 2, 3 , 4 , 5 , 6, 7 , 8])
print(a.ndim)
b = a.reshape(2 ,4)
print(b.ndim)

#实例2:ndarray.shape
#shape属性返回的是元组，元组的长度等于数组的秩，元组中的元素为各维度大小。
a = np.array([[1 , 2 , 3], [4 , 5 , 6]])
print(a.shape)

#调整数组大小:直接修改shape属性
a.shape = (3, 2)
print(a)

#调整数组大小:使用reshape方法
#reshape(shape, order='C')
#shape：数组的维度，可以是整数、元组、列表等。
#order：内存布局，默认为'C'，表示按行优先存储。('C'为行优先，'F'为列优先)
b = a.reshape(2 , 3)
print(b)

#实例3:ndarray.size与ndarray.dtype
#size属性返回数组的元素总数，dtype属性返回数组元素的数据类型。
print(a.size)
print(a.dtype)

#实例4:ndarray.itemsize
#itemsize属性返回数组元素的字节大小。
x = np.array([1 , 2 , 3] , dtype = np.int8)
print(x.itemsize)

y = np.array([1 , 2 , 3] , dtype = np.float64)
print(y.itemsize)

#实例5:ndarray.flags
'''
flags属性返回数组的内存信息。主要包含以下信息：
C_CONTIGUOUS (C)：数组是否为连续存储的。
F_CONTIGUOUS (F)：数组是否为列存储的。
OWNDATA (O)：数组是否拥有内存。
WRITEABLE (W)：数组元素是否可写
ALIGNED (A)：数组元素是否对齐。
UPDATEIFCOPY (U)：数组是否为视图，且数据是否需要更新。
'''
print(a.flags)


#4.Numpy创建数组

'''
基本语法：(除了使用ndarray构造器外)
(1)numpy.empty(shape, dtype=float, order='C') 创建一个未初始化的数组。
shape：数组的维度，可以是整数、元组、列表等。
dtype：数组元素的数据类型，默认为float。
order：内存布局，默认为'C'，表示按行优先存储。('C'为行优先，'F'为列优先)

(2)numpy.zeros(shape, dtype=float, order='C') 创建一个全零数组。
shape：数组的维度，可以是整数、元组、列表等。
dtype：数组元素的数据类型，默认为float。
order：内存布局，默认为'C'，表示按行优先存储。('C'为行优先，'F'为列优先)

(3)numpy.ones(shape, dtype=float, order='C') 创建一个全一数组。
shape：数组的维度，可以是整数、元组、列表等。
dtype：数组元素的数据类型，默认为float。
order：内存布局，默认为'C'，表示按行优先存储。('C'为行优先，'F'为列优先)

(4)numpy.zeros_like(a, dtype=None, order='K', subok=True , shape=None) 创建一个全零数组，与a具有相同的维度和数据类型。
a：给定的数组。
dtype：数组元素的数据类型，默认为None，表示与a相同。
order：内存布局，默认为'K'(保留a的存储顺序)，可选'C'、'F'。
subok：布尔值，默认为True，表示返回的数组是否为子类。
shape：数组的维度，可以是整数、元组、列表等，默认为None，表示与a相同。

(5)numpy.ones_like(a, dtype=None, order='K', subok=True , shape=None) 创建一个全一数组，与a具有相同的维度和数据类型。
a：给定的数组。
dtype：数组元素的数据类型，默认为None，表示与a相同。
order：内存布局，默认为'K'(保留a的存储顺序)，可选'C'、'F'。
subok：布尔值，默认为True，表示返回的数组是否为子类。
shape：数组的维度，可以是整数、元组、列表等，默认为None，表示与a相同。

(6)numpy.random.randn(d0, d1, ..., dn) 创建一个服从正态分布的随机数组。
d0, d1, ..., dn：数组的维度，为整数。

(7)numpy.random.rand(d0, d1, ..., dn) 创建一个服从[0,1)均匀分布的随机数组。
d0, d1, ..., dn：数组的维度，为整数。

(8)numpy.random.randint(low, high=None, size=None, dtype='l') 创建一个服从[low,high)均匀分布的随机整数数组。
low：整数，数组元素的最小值。
high：整数，数组元素的最大值，默认为None，表示high取值范围为[0,low)。
size：数组的维度，可以是整数、元组、列表等，默认为None，表示返回一个单一值。
dtype：数组元素的数据类型，默认为'l'，表示返回整数数组。

(9)numpy.eye(N, M=None, k=0, dtype=float) 创建一个对角线为1，其余元素为0的二维数组。
N：整数，数组的行数。
M：整数，数组的列数，默认为None，表示列数等于行数。
k：整数，对角线的偏移量，默认为0。
dtype：数组元素的数据类型，默认为float。
'''
print("===========================================")

#实例1:numpy.empty
a = np.empty([2 , 3] , dtype = int) #创建未初始化的数组, 此时元素随机
print(a)

#实例2:numpy.zeros
#默认为浮点数
x = np.zeros(5)
print(x)

#指定数据类型
y = np.zeros((5 ,) , dtype = int)
print(y)

#自定义类型
z = np.zeros((2 , 2) , dtype = [('x' , 'i4') , ('y' , 'i4')])
print(z)

#实例3:numpy.ones
#默认为浮点数
x = np.ones(5)
print(x)

#自定义类型
x = np.ones([2 , 2] , dtype = int)
print(x)

#实例4:numpy.zeros_like
a = np.array([[1 , 2 , 3], [4 , 5 , 6]])
b = np.zeros_like(a)
print(b)

#实例5:numpy.ones_like
a = np.array([[1 , 2 , 3], [4 , 5 , 6] , [7 , 8 , 9]])
b = np.ones_like(a)
print(b)

#实例6:numpy.random.randn
a = np.random.randn(2 , 3)
print(a)

#实例7:numpy.random.rand
a = np.random.rand(2 , 3)
print(a)

#实例8:numpy.random.randint
a = np.random.randint(10 , 20 , (2 , 3))
print(a)

#实例9:numpy.eye
a = np.eye(3)
print(a)
a = np.eye(3 , dtype = [('x' , 'i4') , ('y' , 'i4')])
print(a)


#5.Numpy从已有数组创建数组

'''
基本语法：
(1)numpy.asarray(a, dtype=None, order=None) 将输入转换为数组。
a：输入对象，可以是列表、元组、元组列表等。
dtype：数组元素的数据类型，默认为None，表示由输入对象推断。
order：内存布局，默认为None，表示保持输入数组的内存布局。

(2)numpy.frombuffer(buffer, dtype=float, count=-1, offset=0) 从缓冲区创建一个数组。
buffer：缓冲区对象，可以是字节串、缓冲区、内存映射文件等。注意：buffer是字符串时，需要用b前缀表示(如b'123456')。
dtype：数组元素的数据类型，默认为float。
count：数组元素的数量，默认为-1，表示从缓冲区读取所有元素。
offset：缓冲区的偏移量，默认为0。

(3)numpy.fromiter(iterable, dtype, count=-1) 从可迭代对象创建一个数组。
iterable：可迭代对象，如列表、元组、生成器等。
dtype：数组元素的数据类型。
count：数组元素的数量，默认为-1，表示从可迭代对象读取所有元素。
'''
print("===========================================")

#实例1:numpy.asarray
#将列表转换为数组
x = [1 ,2, 3]
a = np.asarray(x)
print(a)

#将元组转换为数组
x = (1 ,2, 3)
a = np.asarray(x)
print(a)

#将元组列表转换为数组
x = [(1, 2), (4, 5)] #numpy数组要求所有元素维度一致，即长度各元组长度相同
a = np.asarray(x)
print(a)

#设置dtype参数
x = [1 , 2,  3]
a = np.asarray(x , dtype = float)
print(a)

#实例2:numpy.frombuffer
s = b'Hello  World'
a = np.frombuffer(s , dtype = 'S1')
print(a)

#实例3:numpy.fromiter
#使用range函数创建列表对象
list = range(5)
it = iter(list)

#使用迭代器创建ndarray
x = np.fromiter(it , dtype = float)
print(x)


#6.Numpy从数据范围创建数组

'''
基本语法：
(1)numpy.arange(start , stop , step , dtype) 创建一个等差数组。
start：数组的起始值(包含,默认为0)。
stop：数组的终止值(不包含)。
step：数组的步长。
dtype：数组元素的数据类型，默认为None，表示由输入对象推断。

(2)numpy.linspace(start , stop , num=50 , endpoint=True , retstep=False , dtype=None) 创建一个等间距数组,将范围均匀分成num个元素。
start：数组的起始值(包含,默认为0)。
stop：数组的终止值(若endpoint为True,则包含)。
num：数组的元素个数，默认为50。
endpoint：布尔值，默认为True，表示包含终止值。
retstep：布尔值，默认为False，表示返回步长。
dtype：数组元素的数据类型，默认为None，表示由输入对象推断。

(3)numpy.logspace(start , stop , num=50 , endpoint=True , base=10.0 , dtype=None) 创建一个等比数列，范围为base^start和base^stop之间，且元素个数为num。
start：数组的起始指数(包含，即base^start)。
stop：数组的终止指数(若endpoint为True,则包含)。
num：数组的元素个数，默认为50。
endpoint：布尔值，默认为True，表示包含终止值。
base：对数底，默认为10。
dtype：数组元素的数据类型，默认为None，表示由输入对象推断。

(4)numpy.geomspace(start , stop , num=50 , endpoint=True , dtype=None) 创建一个等比数列，范围为start和stop之间，且元素个数为num。
start：数组的起始值(包含,默认为10^start)。
stop：数组的终止值(若endpoint为True,则包含)。
num：数组的元素个数，默认为50。
endpoint：布尔值，默认为True，表示包含终止值。
dtype：数组元素的数据类型，默认为None，表示由输入对象推断。
'''
print("===========================================")

#实例1:numpy.arrange
#只有stop参数
x = np.arange(5)
print(x)

#设置返回类型
x = np.arange(5 , dtype = float)
print(x)

#设置start、stop、step
x = np.arange(10 , 20 , 2)
print(x)

#实例2:numpy.linspace
#默认endpoint=True
a = np.linspace(1 , 10 , 10)
print(a)

#默认不返回步长
a = np.linspace(1 , 10, 10 , retstep = True)
print(a)

#扩展
b = np.linspace(1 , 10 , 10).reshape(10 , 1)
print(b)

#实例3:numpy.logspace
#默认指数以10为底
a = np.logspace(1 , 2 , 10)
print(a)

#设置base
a = np.logspace(0 , 9 , 10 , base = 2)
print(a)

#实例4:numpy.geomspace
a = np.geomspace(1 , 10 , 10)
print(a)


#7.Numpy切片和索引

'''
基本语法：与Python列表切片和索引语法一致。
(1)ndarray[indices]：返回指定位置的元素或元素组成的数组。
indices：整数、整数列表、布尔数组、整数数组、整数元组、整数元组列表等，指定要获取元素的位置。

(2)ndarray[indices] = value：将value赋值给指定位置的元素。
indices：整数、整数列表、布尔数组、整数数组、整数元组、整数元组列表等，指定要赋值的元素位置。
value：要赋值的元素值。

(3)切片对象：slice(start, stop, step)
start：整数，切片的起始位置。
stop：整数，切片的终止位置(不包含)。
step：整数，切片的步长。
切片向量既可以为array，也可以为list。

(4)ndarray[lower:upper:step]：返回指定范围内的元素或元素组成的数组。
lower：整数，指定范围的起始位置。
upper：整数，指定范围的终止位置(不包含)。
step：整数，指定步长。
注：关于冒号：
只放置一个参数：返回单个元素。
- 省略lower时，默认为0。
- 省略upper时，默认为数组长度。
- 省略step/只有一个冒号时，默认为1。

(5)返回指定位置的元素或元素组成的数组。
ndarray[indices, ...]: 等价于ndarray[indices][...], 即先索引后切片,表示第indices行元素。
ndarray[... , indices]: 等价于ndarray[...][indices], 即先切片后索引，表示第indices列元素。
注：...表示某一维的全部元素，等价于:，可以用切片对象表示，如如ndarray[indices, 2:5]表示第indices行的第2到第4列元素。
indices表示的维度也可以切片，如ndarray[1:, ...]表示第2行到最后一行的所有元素。
'''
print("===========================================")

#实例1:ndarray[indices]
a = np.array([[1 , 2 , 3], [4 , 5 , 6], [7 , 8 , 9]])
print(a[1]) #返回第2行
print(a[1, 2]) #返回第2行第3列

#实例2:ndarray[indices] = value
a = np.array([[1 , 2 , 3], [4 , 5 , 6], [7 , 8 , 9]])
a[1, 2] = 10
print(a)

#实例3:切片对象
a = np.arange(10)
s = slice(2 , 7 , 2)
print(a[s])

#实例4:直接切片
a = np.arange(10)
b = a[2:7:2]
print(b)

#实例5:省略参数
#返回单个元素：同直接索引

#省略lower时，默认为0
a = np.arange(10)
print(a[:5])

#省略upper时，默认为数组长度
a = np.arange(10)
print(a[2:])

#省略step/只有一个冒号时，默认为1
a = np.arange(10)
print(a[2:5])

#实例6:对于多维数组的切片
a = np.array([[1, 2, 3] , [4, 5, 6] , [7, 8, 9]])
print(a[1:]) #返回第2行到最后一行的所有元素
print(a[...,1]) #返回第2列的所有元素
print(a[1,:]) #返回第2行的所有元素
print(a[...,1:]) #返回第2列到最后一列的所有元素
print(a[1:2, 1:3]) #返回第2行第2列到第2行第3列的所有元素


#8.Numpy数组的高级索引
print("===========================================")

#整数索引：使用整数数组进行索引，可以同时选择多个元素。
#实例1:简单索引
x = np.array([[1 , 2] , [3 , 4] , [5 , 6]])
y = x[[0 , 1 ,2] , [0 , 1 , 0]] #选择(0 , 0) , (1 , 1) , (2 , 0)三个元素组成的数组
print(y)

#实例2:复合索引
x = np.array([[0 , 1 , 2] , [3 , 4 , 5] , [6 , 7 , 8] , [9 , 10, 11]])
rows = np.array([[0 , 0] , [3 ,3]])
cols = np.array([[0 , 2] , [0 ,2]])
y = x[rows, cols] #选择(0 , 0) , (0 , 2) , (3 , 0) , (3 , 2)四个元素组成的数组
print(y)

#注：可以借助切片和整数索引进行更复杂的索引操作。对于二维数组要求索引数组维度一致。

#布尔索引：使用布尔数组进行索引，可以选择满足条件的元素。
#实例3：挑选式
x = np.array([[1 , 2] , [3 , 4] , [5 , 6]])
print(x[x > 2]) #选择元素值大于2的元素组成的数组

#实例4:过滤式
x = np.array([np.nan , 1 , 2, np.nan , 3 , 4 , 5])
print(x[~np.isnan(x)]) #选择非NaN元素组成的数组

a = np.array([1 , 2+6j , 5 , 3.5+5j])
print(a[np.iscomplex(a)]) #选择复数元素组成的数组

#注:numpy.nan表示Not a Number，即非数值。
#np.isnan()函数可以判断元素是否为NaN。
#np.iscomplex()函数可以判断元素是否为复数。
#布尔索引可以与切片组合使用。如：x[x[...,0] > 2] 表示选择x的第0维大于2的元素组成的数组。

#花式索引：使用整数数组进行索引，可以同时选择多个元素，且可以指定索引的顺序(类似整数索引)。
#实例5:一维数组
x = np.arange(10)
y = x[[6 , 0]] #选择第6、0个元素组成的数组(有序)
print(y)

#实例6:二维数组
x = np.arange(32).reshape(8 , 4)
print(x[[4 , 2 , 1 , 7]]) #选择第4、2、1、7行组成的数组(有序)

#实例7:传入多个索引数组(np.ix_)
#np.ix_()：输入两个数组进行笛卡尔积，返回两个数组的笛卡尔积的索引。
x = np.arange(32).reshape(8 , 4)
print(x[np.ix_([1,5,7,2],[0,3,1,2])])

#补充:关于多条件的布尔索引
#print(x[x > 5 & x < 10]) 会报错，因为x>5&x<10是多条件的布尔表达式，不能直接作为索引。
#方法1：加上括号
print(x[(x > 5) & (x < 10)])

#方法2：使用np.logical_and方法
print(x[np.logical_and(x > 5 , x < 10)])

#方法3：使用np.all方法
print(x[np.all([x > 5 , x < 10], axis=0)])
#注：axis=0表示对行进行操作，axis=1表示对列进行操作。


#9.Numpy广播机制
print("===========================================")

#当两个数组形状相同时，则运算为对应位的运算
#实例1:相同形状
a = np.array([1 , 2, 3 , 4])
b = np.array([10 , 20 ,30 , 40])
c = a * b
print(c)

#当两个数组形状不同时，会发生广播机制
#实例2:不同形状
a = np.array([[0 , 0 , 0],[10 , 10 , 10] , [20 , 20 , 20], [30 , 30 , 30]])
b = np.array([0 , 1, 2])
print(a + b)
print(a * b)

'''
广播的规则：
(1)所有输入的数组都向其中形状最长的数组看齐，形状中不足的部分通过在前面加1补齐。
(2)输出数组的形状是输入数组形状的各个维度上的最大值。
(3)如果输入的数组的某维度和输出数组对应维度的长度相同或者其长度为1时，这个数组能够用来计算，否则出错
(4)当输入的数组的某个维度长度为1时，沿着此维度运算时都用此维度上的第一组值
简单来说，对于两个数组，分别比较它们的每一个维度(若其中一个数组没有当前维度则忽略)，满足:
- 数组拥有相同的形状
- 当前维度的值相等
- 当前维度的值有一个是1
则可以进行广播运算。
'''

#补充:numpy.tile()函数
'''
基本语法:
numpy.tile(A, reps)
A：数组。
reps：整数元组，表示需要重复的次数。
如果reps是一个数，就是简单的将A向右复制reps-1次形成新的数组。
如果reps是一个元组/列表/数组类型的，有两个元素，如[m , n]，实际上就是将A变成m*n个A组成的新数组，有m行n列个A。
'''
#实例1:简单复制
a = np.array([[1 , 2] , [3 , 4]])
print(np.tile(a , 2))

#实例2:复制成m*n个A
print(np.tile(a , [2 , 3]))


#10.Numpy迭代数组

'''
基本语法：
for i in numpy.nditer(array , order='C' , op_flags=[] , flags=[])
array：数组。
order：'C'(按行)或'F'(按列)，表示数组的存储顺序。
op_flags：指定迭代器的操作类型：
- 'readwrite'：可读写。
- 'readonly'：只读。
- 'writeonly'：只写。
- 'no_broadcast'：禁止广播。
- 'reduce_ok'：允许减少维度。
- 'grow_inner'：允许增加内部维度。
- 'grow_outer'：允许增加外部维度。
flags：指定迭代器的附加选项：
- c_index：以C语言风格的索引方式迭代。
- f_index：以Fortran语言风格的索引方式迭代。
- multi_index：每次迭代可以跟踪一种索引类型。
- external_loop：给出的值是具有多个值的一维数组，而不是零维数组。
'''
print("===========================================")

#实例1:迭代数组
a = np.arange(6).reshape(2 , 3)
for x in np.nditer(a):
    print(x , end = ', ')
print()

#实例2:控制迭代顺序
a = np.arange(6).reshape(2 , 3)
for x in np.nditer(a , order = 'F'):
    print(x , end = ', ')
print()

#实例3:修改数组中元素的值
#默认情况下，迭代器是只读的，不能修改数组的值。可以通过op_flags参数指定可读写的迭代器。
a = np.arange(6).reshape(2 , 3)
for x in np.nditer(a , op_flags=['readwrite']):
    x[...] = 2*x #修改数组元素的值，x[...]是修改原numpy元素
print(a)

#实例4:使用外部循环
#external_loop参数可以给出具有多个值的一维数组，而不是零维数组。
a = np.arange(6).reshape(2 , 3)
for x in np.nditer(a , flags=['external_loop'] , order='F'):
    print(x , end = ', ')
print()

#实例5:广播迭代
#如果两个数组是可以广播的，则迭代器会同时迭代两个数组的元素。
a = np.arange(6).reshape(2 , 3)
b = np.array([10 , 20 , 30])
for x,y in np.nditer([a , b]):
    print("%d:%d" % (x , y) , end = ',')
print()


#11.Numpy数组操作

'''
基本语法：
(1)修改数组形状：
·numpy.reshape(arr , newshape , order='C') #不修改数据的条件下修改数组形状
arr：数组。
newshape：整数或者整数数组，表示目标形状。
order：'C'(按行)或'F'(按列)或'A'(保持原数组的存储顺序)或'K'(保持原数组的元素顺序)，表示数组的存储顺序。
等价于arr.reshape(newshape , order)

·ndarray.flat #数组元素迭代器

·ndarray.flatten(order='C') #返回一份数组展开(1维)的副本，不改变原数组
order：'C'(按行)或'F'(按列)或'A'(保持原数组的存储顺序)或'K'(保持原数组的元素顺序)，表示数组的存储顺序。

·numpy.ravel(arr , order='C') #展开原始数据(1维)(改变原数组，不产生新数组)
arr：数组。
order：'C'(按行)或'F'(按列)或'A'(保持原数组的存储顺序)或'K'(保持原数组的元素顺序)，表示数组的存储顺序。
等价于arr.ravel(order)

(2)翻转数组
·numpy.transpose(arr , axes=None) #对换数组的维度(转置)
arr：要操作的数组。
axes：整数列表/元组，表示维度的顺序，通常所有维度都会对换。

·ndarray.T #等价于numpy.transpose(arr), 即对换数组的维度(转置)

·numpy.rolllaxis(arr , axis , start) #沿着指定轴滚动数组元素
arr：数组。
axis：整数，指定滚动的轴，其他轴的相对位置不变。
start：整数，指定滚动的起始位置，默认值为0。

·numpy.swapaxes(arr , axis1 , axis2) #交换两个轴的位置
arr：数组。
axis1：整数，指定第一个轴。
axis2：整数，指定第二个轴。

(3)修改数组的维度
·numpy.broadcast(arr1 , arr2 , subok=True) #广播两个数组(arr2广播到arr1)，返回值具有iterator属性，可以迭代得到广播后的数组
arr1：数组。
arr2：数组。
subok：布尔值，如果为True，则允许子类化，否则禁止子类化。

·numpu.broadcast_to(arr , shape , subok=True) #广播数组到指定形状, 返回广播后的数组
arr：数组。
shape：整数元组，表示目标形状。
subok：布尔值，如果为True，则允许子类化，否则禁止子类化。

·numpy.expand_dims(arr , axis) #在指定轴上增加新的维度
arr：数组。
axis：整数，指定增加维度的轴。

·numpy.squeeze(arr , axis) #删除指定轴上的维度
arr：数组。
axis：整数或整数列表/元组，指定要删除的轴，默认值为None，表示删除所有长度为1(无元素高维或者单元素最低维)的轴。

(4)连接数组
·numpy.concatenate((a1 , a2 , ...), axis) #沿指定轴连接相同形状的数组
a1、 a2、...： 相同类型的数组。
axis：整数，指定连接的轴，默认值为0。

·numpy.stack((a1 , a2 , ...), axis=0) #沿指定新轴堆叠数组
a1、 a2、...： 相同类型的数组。
axis：整数，指定堆叠的轴，默认值为0。

·numpy.hstack((a1 , a2 , ...)) #沿水平轴连接数组
a1、 a2、...： 相同类型的数组。

·numpy.vstack((a1 , a2 , ...)) #沿垂直轴连接数组
a1、 a2、...： 相同类型的数组。

(5)分割数组
·numpy.split(arr , indices_or_sections , axis) #分割数组
arr：被分割的数组。
indices_or_sections：如果是个整数，则用该数平均切分，如果是一个数组，为沿轴切分的位置(左开右闭)，默认值为1。
axis：整数，指定分割的轴，默认值为0，为0时表示沿行切分，为1时表示沿列切分。

·numpy.hsplit(arr , indices_or_sections) #沿水平轴分割数组
arr：被分割的数组。
indices_or_sections：如果是个整数，则用该数平均切分，如果是一个数组，为沿轴切分的位置(左开右闭)，默认值为1。

·numpy.vsplit(arr , indices_or_sections) #沿垂直轴分割数组
arr：被分割的数组。
indices_or_sections：如果是个整数，则用该数平均切分，如果是一个数组，为沿轴切分的位置(左开右闭)，默认值为1。

(6)数组元素的添加与删除
·numpy.resize(arr ,shape) #改变数组的形状，当尺寸变大时会填充重复的行/列，当尺寸变小时会截断数组
arr：数组。
shape：整数元组，表示目标形状。

·numpy.append(arr , values , axis=None) #在指定轴上添加元素
arr：数组。
values：数组，指定要添加的元素，与arr的形状相同。
axis：整数，指定轴，默认值为None，表示展开后横向加成，返回总为一维数组。当axis为0时，表示纵向加成(下)，当axis为1时，表示横向加成(右)。

·numpy.insert(arr , obj , values , axis=None) #在指定轴上指定索引位置插入元素
arr：数组。
obj：在其之前插入值的索引
values：数组，指定要插入的元素，与arr的形状相同。
axis：整数，指定轴，默认值为None，表示展开后横向插入，返回总为一维数组。当axis为0时，表示纵向插入，当axis为1时，表示横向插入。

·numpy.delete(arr , obj , axis=None) #删除指定轴上的元素
arr：数组。
obj：可以被切片，整数或整数数组，指定要删除的元素的索引。
axis：整数，指定轴，默认值为None，表示展开后横向删除，返回总为一维数组。当axis为0时，表示纵向删除，当axis为1时，表示横向删除。

·numpy.unique(arr , return_index=False , return_inverse , return_counts) #去重
arr：数组，如果不是一维数组，则展开后再去重。
return_index：布尔值，默认值为False，如果为True，则返回去重元素在原数组中的索引，并以列表形式储存。
return_inverse：布尔值，默认值为False，如果为True，则返回原数组中每个元素的索引在去重后的数组中的索引，并以列表形式储存。
return_counts：布尔值，默认为False，如果为True，则返回每个去重元素的出现次数。
'''

#实例1：numpy.reshape()
a = np.arange(8).reshape(4 , 2)
print(a)

#实例2：ndarray.flat
a = np.arange(9).reshape(3 , 3)
for e in a.flat:
    print(e)

#实例3:ndarray.flatten
a = np.arange(8).reshape(2 , 4)
print(a.flatten())
print(a.flatten(order = 'F'))

#实例4:numpy.ravel
a = np.arange(8).reshape(2 , 4)
print(a.ravel())
print(a.ravel(order = 'F'))

#实例5:numpy.transpose
a = np.arange(12).reshape(3 , 4)
print(np.transpose(a))

#实例6:ndarray.T
a = np.arange(12).reshape(3 , 4)
print(a.T)

#实例7:numpy.rollaxis
a = np.arange(8).reshape(2 , 2,  2)
print(np.where(a == 6)) #np.where()返回数组中满足条件的元素的索引
b = np.rollaxis(a,2,0) #将轴2滚动到轴0(宽度到深度)
print(b)
print(np.where(b == 6))

#实例8:numpy.swapaxes
a = np.arange(8).reshape(2 , 2 , 2)
print(np.swapaxes(a , 2 , 0)) # 交换轴2和轴0

#实例9:numpy.broadcast
x = np.array([[1] , [2] , [3]])
y = np.array([4 , 5 , 6])
b = np.broadcast(x , y) #对y广播x
for i in b:
    print(i)
print()
r , c = b.iters #r,c分别为广播后的x的行数和列数
print(next(r) , next(c)) #next()函数返回迭代器的下一个元素
print(next(r) , next(c))

#补充：手动使用broadcast将x和y相加
c = np.empty(b.shape)
c.flat = [u + v for (u , v) in b] #推导式
print(c)

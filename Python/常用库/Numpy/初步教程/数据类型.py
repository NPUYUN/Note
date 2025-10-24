# Numpy数据类型
"""
Numpy支持的数据类型比Python内置的数据类型要丰富得多，基本上可以与C语言的数据类型对应。

Numpy常见数据类型有：
- bool_：布尔型，True或False
- int_：默认的整数类型(类似C语言中的long, int32或int64)
- intc：与C语言中的C语言类型一致，一般为int32或int64
- intp：用于索引的整数类型，类似C语言中的ssize_t，一般为int32或int64
- int8, int16, int32, int64：8, 16, 32, 64位有符号整数
- uint8, uint16, uint32, uint64：8, 16, 32, 64位无符号整数
- float16, float32, float64：16, 32, 64位浮点数
- complex64, complex128：32, 64位复数

Numpy的数值类型实际上是dtype对象的实例，并对应唯一的字符，包括np.bool_、np.int_、np.float_、np.complex_等。
"""
import numpy as np

"""
数据类型对象：dtype

数据类型对象描述了数据的类型、大小、字节顺序等信息
其中字节顺序是通过对数据类型预先设定的<和>来决定的，大端法和小端法分别对应于'>'和'<'。

dtype对象可以用以下方式创建：
numpy.dtype(object, align=False, copy=True)
参数说明：
- object：要转换为的数据类型对象
- align：若为True，填充字段使其类型C的结构体
- copy：复制dtype对象，如果为False，则是对内置数据类型对象的引用
"""

# 实例1
a = np.dtype(np.int32)
print(a)

# 实例2
# int8, int16, int32, int64可以使用字符串'i1', 'i2', 'i4', 'i8'表示
a = np.dtype('i4')
print(a)

# 实例3：标注字节顺序
a = np.dtype('<i4')
print(a)

# 实例4：结构化数据类型
a = np.dtype([('age' , np.int32)])
print(a)

# 实例5，将数据类型应用于ndarray
b = np.array([(10,) , (20,) , (30,)] , dtype=a)
print(b)

# 实例6：根据字段名存取实际的列
print(b['age'])

# 示例：
student = np.dtype([('name', 'S20'), ('age', 'i4'), ('gender', 'S1')])
data = np.array([('Alice', 20, 'F'), ('Bob', 25, 'M')], dtype=student)
print(data) # 字符串前出现b：表示字节类型

"""
补充：为什么i4代表int32?

每一个内建类型都有唯一定义他们的字符代码：
- b：布尔型
- i：整数型
- u：无符号整数型
- f：浮点型
- c：复数型
- m：timedelta型
- M：datetime型
- O：对象型
- S：字符串型
- U：Unicode字符串型
- V：原始数据（void）型

其中i代表integer，4代表4字节。所以i4代表int32。即字符代码后面跟着的数字代表字节数。
"""

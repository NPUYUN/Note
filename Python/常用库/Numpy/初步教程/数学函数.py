# Numpy 数学函数

import numpy as np
"""
Numpy包含了大量的各种数学运算的函数，包括：
在没有特殊说明的情况下，以下函数的参数列表均含有(out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True)，具体含义如下：
- out：输出数组，可选。
- where：布尔数组，指定输出数组中参与计算的元素的位置，可选。
- casting：数组类型转换的规则，可选。
- order：输出数组的内存布局，可选。
- dtype：输出数组的数据类型，可选。
- subok：默认返回一个与输入数组相同类型的数组，如果为True，则返回一个子类数组。
下列函数中，...表示省略该参数列表

1. 三角函数
(1) 三角函数
numpy.sin(x, ...), numpy.cos(x, ...), numpy.tan(x, ...)
- x：弧度值数组

反三角函数：numpy.arcsin(x, ...), numpy.arccos(x, ...), numpy.arctan(x, ...)
- x：正弦值、余弦值、正切值数组


(2) 角度和弧度之间的转换：
角度转弧度：numpy.deg2rad(x, ...)
- x：角度值数组
 
弧度转角度：numpy.rad2deg(x, ...)
- x：弧度值数组


(3) 象限反正切：
numpy.arctan2(y , x, ...)
- y：纵坐标数组
- x：横坐标数组


(4) 直角三角形斜边计算：
numpy.hypot(x1 , x2, ...)
- x1：一条直角边的长度数组
- x2：另一条直角边的长度数组


(5) 角度展开：
numpy.unwrap(p , discont=2*np.pi, axis=-1, period=None)
- p：角度数组
- discont：连续的角度值间隔，默认值为2*pi
- axis：沿着哪个轴计算，默认值为-1(最后一个轴)
- period：周期，默认值为2*pi
把 “跳变的角度”（比如从接近 2π 突然跳到 0）调整成连续的角度序列


2. 双曲函数
(1) 双曲函数
numpy.sinh(x, ...), numpy.cosh(x, ...), numpy.tanh(x, ...)
- x：输入数组

(2) 反双曲函数
numpy.arcsinh(x, ...), numpy.arccosh(x, ...), numpy.arctanh(x, ...)
- x：输入数组


3. 舍入函数
(1) 四舍六入五取偶：numpy.around(x , decimals=0, ...)/numpy.round(x, decimals=0, ...)
- x：输入数组
- decimals：保留的小数位数，默认值为0(四舍五入到整数)
注意：四舍六入五取偶(银行家舍入法)：当恰好为0.5时，向偶数舍入(如2.5->2, 3.5->4)

(2) 最近整数：numpy.fix(x, ...)
- x：输入数组

(3) 向上取整：numpy.ceil(x, ...)
- x：输入数组

(4) 向下取整：numpy.floor(x, ...)
- x：输入数组

(5) 截断取整：numpy.trunc(x, ...)
- x：输入数组

(6) 整数与小数分离：numpy.modf(x, out1=None, out2=None, ...)
- x：输入数组
- out1：整数部分的输出数组
- out2：小数部分的输出数组
注意：numpy.modf()返回的是一个元组，第一个元素是整数部分，第二个元素是小数部分。


4. 指数和对数函数
(1) 指数：numpy.exp(x, ...)
- x：输入数组

(2) 平方根：numpy.sqrt(x, ...)
- x：大于0的输入数组

(3) 平方：numpy.square(x, ...)
- x：输入数组

(4) 自然对数：numpy.log(x, ...)
- x：大于0的输入数组

(5) 2的对数：numpy.log2(x ,...)
- x：大于0的输入数组

(6) 10的对数：numpy.log10(x, ...)
- x：大于0的输入数组

(7) 自然对数(1 + x)：numpy.log1p(x, ...)
- x：输入数组

(8) 幂运算：numpy.power(x1, x2, ...)、numpy.float_power(x1, x2, ...)
- x1：底数数组
- x2：指数数组
注意：numpy.float_power()函数结果的类型为浮点数。
"""

# 实例1：三角函数
x = np.array([0, np.pi/6, np.pi/4, 3*np.pi/3, np.pi/2])
print(np.sin(x))

# 实例2：反三角函数
y = np.array([0, 1/2, 1/3, 1/4, 1/5])
print(np.arcsin(y))

# 实例3：角度和弧度之间的转换
a = np.array([0, 30, 45, 60, 90])
print(np.deg2rad(a) / np.pi)
print(np.rad2deg(np.deg2rad(a)))

# 实例4：象限反正切
x = np.array([1, 1, -1, -1])
y = np.array([1, -1, 1, -1])
print(np.arctan2(y, x))

# 实例5：直角三角形斜边计算
a = np.array([3, 4])
b = np.array([4, 3])
print(np.hypot(a, b))

# 实例6：角度展开
p = np.array([0, 9*np.pi/2])
print(np.unwrap(p) / np.pi)

# 实例7：双曲函数与反双曲函数
a = np.array([0, 1, -1, 10])
print(np.sinh(a))
print(np.arcsinh(a))

# 实例8：舍入函数
a = np.array([-2.6, 1.2, 2.5, 3.7, 4.3])
# 四舍五入
print(np.round(a))
# 最近整数
print(np.fix(a))
# 向上取整
print(np.ceil(a))
# 向下取整
print(np.floor(a))
# 截断取整
print(np.trunc(a))
# 整数与小数分离
print(np.modf(a))

# 实例9：指数函数
a = np.array([0, 1, 2, 3, 4])
print(np.exp(a))

# 实例10：平方根函数
a = np.array([0, 1, 4, 9, 16])
print(np.sqrt(a))

# 实例11：平方函数
a = np.array([1, 2, 3, 4, 5])
print(np.square(a))

# 实例12：对数函数
a = np.array([1, 2, 3, 4, 5])
# 自然对数
print(np.log(a))
# 2的对数
print(np.log2(a))
# 10的对数
print(np.log10(a))
# 自然对数(1 + x)
print(np.log1p(a))

# 实例13：幂运算
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])
# 幂运算
print(np.power(a, b))
# 幂运算结果的类型为浮点数
print(np.float_power(a, b))
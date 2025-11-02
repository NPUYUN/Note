# Numpy 统计函数

import numpy as np

"""
Numpy提供了很多统计函数，可以方便地对数组进行统计计算。
1. 聚合运算函数
(1) numpy.sum(a, axis=None, dtype=None, out=None, keepdims=False, initial=None, where=True)
计算数组a沿着指定轴axis的元素的和。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- dtype：输出数组的数据类型。
- out：输出数组。
- keepdims：是否保持缩减的维度。
- initial：累计初始值。
- where：布尔数组，用于指定计算哪些元素。

(2) numpy.mean(a, axis=None, dtype=None, out=None, keepdims=False, where=True)
计算数组a沿着指定轴axis的元素的平均值。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- dtype：输出数组的数据类型。
- out：输出数组。
- keepdims：是否保持缩减的维度。
- where：布尔数组，用于指定计算哪些元素。

(3) numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=False)
计算数组a沿着指定轴axis的元素的中位数。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- out：输出数组。
- overwrite_input：允许修改输入数组以节省内存。
- keepdims：是否保持缩减的维度。

(4) numpy.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False, where=True)
计算数组a沿着指定轴axis的元素的方差。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- dtype：输出数组的数据类型。
- out：输出数组。
- ddof：自由度(默认为0，计算总体方差；如果为1，计算样本方差)
- keepdims：是否保持缩减的维度。
- where：布尔数组，用于指定计算哪些元素。

(5) numpy.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False, where=True)
计算数组a沿着指定轴axis的元素的标准差。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- dtype：输出数组的数据类型。
- out：输出数组。
- ddof：自由度(默认为0，计算总体标准差；如果为1，计算样本标准差)
- keepdims：是否保持缩减的维度。
- where：布尔数组，用于指定计算哪些元素。

(6) numpy.average(a, axis=None, weights=None, returned=False, keepdims=False)
计算数组a沿着指定轴axis的元素的加权平均值。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- weights：权重数组。
- returned：是否返回均值、方差、标准差。
- keepdims：是否保持缩减的维度。


2. 极值分析函数
(1) numpy.amax(a, axis=None, out=None, keepdims=False, initial=-inf, where=True)
计算数组a沿着指定轴axis的元素的最大值。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- out：输出数组。
- keepdims：是否保持缩减的维度。
- initial：初始值，默认为-inf，用于空数组。
- where：布尔数组，用于指定计算哪些元素。

(2) numpy.amin(a, axis=None, out=None, keepdims=False, initial=inf, where=True)
计算数组a沿着指定轴axis的元素的最小值。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- out：输出数组。
- keepdims：是否保持缩减的维度。
- initial：初始值，默认为inf，用于空数组。
- where：布尔数组，用于指定计算哪些元素。

(3) numpy.ptp(a, axis=None, out=None, keepdims=False)
计算数组a沿着指定轴axis的元素的最大值与最小值的差。
- a：输入数组。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- out：输出数组。
- keepdims：是否保持缩减的维度。


3. 分位数计算函数
(1) numpy.percentile(a, q, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False)
计算数组a沿着指定轴axis的元素的第q分百位数。
- a：输入数组。
- q：分位数(0-100)。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- out：输出数组。
- overwrite_input：允许修改输入数组以节省内存。
- interpolation：插值方法(有linear(线性插值)、lower(低估)、higher(高估)、midpoint(中点)、nearest(最近邻)五种)。
- keepdims：是否保持缩减的维度。

(2) numpy,quantile(a, q, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False)
计算数组a沿着指定轴axis的元素的第q分位数。
- a：输入数组。
- q：分位数(0-1)。
- axis：沿着哪个轴计算。如果为None，则沿所有轴计算。
- out：输出数组。
- overwrite_input：允许修改输入数组以节省内存。
- interpolation：插值方法(有linear(线性插值)、lower(低估)、higher(高估)、midpoint(中点)、nearest(最近邻)五种)。
- keepdims：是否保持缩减的维度。


4. 相关性统计函数
(1) numpy.corrcoef(x, y=None, rowvar=True, bias=False, ddof=None, dtype=None)
计算x和y的Pearson相关系数矩阵。
- x：输入数组。
- y：输入数组。
- rowvar：是否按行计算。
- bias：是否使用偏差修正。
- ddof：自由度。
- dtype：输出数组的数据类型。

(2) numpy.cov(m, y=None, rowvar=True, bias=False, ddof=None, fweights=None, aweights=None)
计算m和y的协方差矩阵。
- m：输入数组。
- y：输入数组。
- rowvar：是否按行计算。
- bias：是否使用偏差修正。
- ddof：自由度。
- fweights：样本权重。
- aweights：总体权重。


5. 直方图函数
(1) numpy.histogram(a, bins=10, range=None, normed=None, weights=None, density=None)
计算一维数组a的直方图。
- a：输入数组。
- bins：直方图的区间个数或区间数组。
- range：直方图的区间范围。
- normed：是否将直方图正规化。
- weights：样本权重。
- density：是否将直方图变为概率密度直方图。

(2) numpy.bincount(x, weights=None, minlength=0)
计算数组x中每个值的频数。
- x：输入数组。
- weights：样本权重。
- minlength：输出数组的最小长度。


6. NaN处理函数
numpy.nansum
numpy.nanmean
numpy.nanmedian
numpy.nanvar
numpy.nanstd
numpy.nanmin
numpy.nanmax
numpy.nanpercentile
numpy.nanquantile
参数不变
"""

# 实例1：求和
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(a))
print(np.sum(a, axis=0))

# 实例2：求平均值
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.mean(a))
print(np.mean(a, axis=0))

# 实例3：求中位数
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.median(a))
print(np.median(a, axis=0))

# 实例4：求方差
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.var(a))
print(np.var(a, axis=0))

# 实例5：求标准差
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.std(a))
print(np.std(a, axis=0))

# 实例6：求加权平均值
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1 , 1 , 1] , [2 , 2 , 2]])
print(np.average(a, weights=b))

# 实例7：求最大值
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.amax(a))
print(np.amax(a, axis=0))

# 实例8：求最小值
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.amin(a))
print(np.amin(a, axis=0))

# 实例9：求极差
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.ptp(a))
print(np.ptp(a, axis=0))

# 实例10：求分位数
a = np.array([[1, 2, 3], [4, 5, 6] , [7, 8, 9]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.quantile(a, 0.5))
print(np.quantile(a, 0.5, axis=0))

# 实例11：求相关性
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(np.corrcoef(a, b))

# 实例12：求协方差
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(np.cov(a, b))

# 实例13：求直方图
a = np.array([1, 2, 1, 3, 4, 4, 4])
print(np.histogram(a))

# 实例14：求频数
a = np.array([1, 2, 1, 3, 4, 4, 4])
print(np.bincount(a))
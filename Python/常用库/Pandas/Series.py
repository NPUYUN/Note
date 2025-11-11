# Pandas Series

import pandas as pd
import numpy as np

"""
Series 是 Pandas 库中的一个核心数据结构，类似于一维数组，具有数据和索引。
Series可以存储任何数据类型，并通过标签(索引)来访问元素

1. Series的特点
- 一维数组： Series 是一个一维数组，每个元素都有一个对应的索引。
- 索引： 每个元素都有一个标签(索引)，默认为从0开始的整数索引，也可以自定义索引标签。
- 数据类型： Series 可以存储各种数据类型，如整数、浮点数、字符串等。
- 大小不变性： Series 的大小在创建后是不可变的，但是可以通过某些操作改变
- 操作：Series 支持多种操作，如算术运算、统计计算、过滤等。
- 缺失数据：Series 可以处理缺失数据，使用 NaN 表示缺失值。
- 自动对齐：当多个Series 进行运算时，会根据索引自动对齐数据。


2. 创建 Series
可使用pandas.Series()构造函数来创建一个Series对象。
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
- data: Series的数据部分，可以是列表、数组、字典、标量值等。若不提供此参数，则创建一个空的Series。
- index: 指定Series的索引标签，可以是列表、数组、索引对象等。如果不提供，则默认使用整数索引。
- dtype: 指定Series中数据的类型，可以是Numpy的数据类型。如果不提供，Pandas会根据数据自动推断类型。
- name: Series的名称，可以是字符串或其他类型。
- copy: 是否复制数据，默认为False。若设置为True，则会创建数据的副本。
- fastpath: 是否启用快速路径，默认为False。通常不需要手动设置此参数。


3. Series的基本方法
(1) Series.index: 返回Series的索引对象。
(2) Series.values: 返回Series的数据部分，作为一个NumPy数组。
(3) Series.head(n): 返回Series的前n个元素，默认为5
(4) Series.tail(n): 返回Series的后n个元素，默认为5
(5) Series.dtype: 返回Series中数据的类型
(6) Series.shape: 返回Series的形状(行数)
(7) Series.describe(): 返回Series的统计摘要信息，如计数、均值、标准差、最小值、最大值等。
(8) Series.isnull(): 返回一个布尔Series，表示每个元素是否为缺失值(NaN)。
(9) Series.notnull(): 返回一个布尔Series，表示每个元素是否非缺失值。
(10) Series.unique(): 返回Series中的唯一值数组(去重)。
(11) Series.value_counts(): 返回Series中每个唯一值的出现次数
(12) Series.map(func): 对Series中的每个元素应用一个函数，并返回一个新的Series。
(13) Series.apply(func): 对Series中的每个元素应用一个函数，并返回一个新的Series，常用于自定义操作
(14) Series.astype(dtype): 将Series的数据类型转换为指定的dtype，并返回一个新的Series。
(15) Series.sort_values(ascending=True): 按值对Series进行排序，ascending参数指定是否升序排序。
(16) Series.sort_index(ascending=True): 按索引对Series进行排序，ascending参数指定是否升序排序。
(17) Series.dropna()： 返回一个新的Series，删除所有缺失值(NaN)。
(18) Series.fillna(value)： 返回一个新的Series，将缺失值(NaN)替换为指定的value。
(19) Series.replace(to_replace, value)： 返回一个新的Series，将指定的to_replace值替换为value。
(20) Series.cumsum()： 返回一个新的Series，计算累积和。
(21) Series.cumprod()： 返回一个新的Series，计算累积积。
(22) Series.shift(periods)： 返回一个新的Series，将数据向前或向后移动指定的periods个位置。
(23) Series.rank()： 返回一个新的Series，计算每个元素的排名。
(24) Series.corr(other)： 计算与另一个Series的相关系数(默认为皮尔逊)。
(25) Series.cov(other)： 计算与另一个Series的协方差。
(26) Series.to_list()： 将Series转换为一个Python列表。
(27) Series.to_frame()： 将Series转换为一个DataFrame对象。
(28) Series.iloc[]: 基于整数位置进行索引和切片。
(29) Series.loc[]: 基于标签进行索引和切片。
(30) Series.sum(): 计算Series中所有元素的和。
(31) Series.mean(): 计算Series中所有元素的均值。
(32) Series.median(): 计算Series中所有元素的中位数。
(33) Series.std(): 计算Series中所有元素的标准差。
(34) Series.min(): 返回Series中的最小值。
(35) Series.max(): 返回Series中的最大值。
... 其他方法请参考Pandas官方文档。
"""

# 实例1：创建一个简单的Series
a = [1 , 2 , 3]
x = pd.Series(a)
print(x)

# 实例2：指定索引值
a = ["A" , "B" , "C"]
x = pd.Series(a , index=["x" , "y" , "z"])
print(x)
print(x["x"]) # 通过索引标签访问元素

# 实例3：使用字典创建Series
a = {'a': 10, 'b': 20, 'c': 30}
x = pd.Series(a)
print(x)
# 当只需要字典中的一部分时，只需要指定需要的数据索引即可
y = pd.Series(a , index=["a" , "c"])
print(y)

# 实例4：设置Series的名称
a = [100 , 200 , 300]
x = pd.Series(a , name="My Series")
print(x)

# 实例5：Series的基本方法
a = {"x" : 10, "y" : 20, "z" : 30, "m" : None}
x = pd.Series(a)
print(x.index) # 获取索引
print(x.values) # 获取值
print(x.dtype) # 获取数据类型
print(x.head(2)) # 获取前2个元素

# 使用map将每个元素加倍
x_double = x.map(lambda v: v * 2 if v is not None else v)
print(x_double)

# 计算累计和
print(x.cumsum)

# 查找缺失值
print(x.isnull())

# 排序
x_sort = x.sort_values()
print(x_sort)

# 其他基本操作
print(x['x']) # 通过标签访问元素
print(x['x' : 'z']) # 通过切片访问元素
x['x'] = 50 # 修改元素值
x['n'] = 40 # 通过新索引添加元素
del x['m'] # 删除元素
x_del = x.drop(['x']) # 删除元素，返回新Series
print(x)
print(x_del)

# 基本运算
# 算术运算
x_add = x + 10 # 每个元素加10
print(x_add)

# 过滤
x_filtered = x[x > 15] # 选择大于15的元素
print(x_filtered)

# 数学函数
x_sqrt = np.sqrt(x) # 计算平方根
print(x_sqrt)

# 统计函数
print(x.sum()) # 计算总和
print(x.mean()) # 计算均值
print(x.median()) # 计算中位数
print(x.std()) # 计算标准差
print(x.min()) # 计算最小值
print(x.max()) # 计算最大值
print(x.corr(x_add)) # 计算相关系数
print(x.cov(x_add)) # 计算协方差
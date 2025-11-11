# Pandas DataFrame

import pandas as pd

"""
DataFrame 是 Pandas 库中另一个核心数据结构，类似于一个二维的表格或者数据库中的数据表
DataFrame 是一个表格型数据结构，包含有序的多列，每列可以是不同的数据类型（数值、字符串、布尔值等）
DataFrame 既有行索引也有列索引，可以通过标签或整数位置进行访问，可被看作是 Series 组成的字典
DataFrame 提供了丰富的方法用于数据操作、清洗、分析和可视化等操作

1. DataFrame的特点
- 二维结构：DataFrame 是一个二维的表格结构，包含行和列。可视为多个Series对象组成的字典
- 异构数据类型：DataFrame 的每一列可以包含不同的数据类型，如整数、浮点数、字符串、布尔值等
- 标签索引：DataFrame 既有行索引也有列索引，可以通过标签或整数位置进行访问
- 大小可变：DataFrame 的大小是可变的，可以动态添加或删除行和列
- 自动对齐：在进行算术运算或合并操作时，DataFrame 会根据索引自动对齐数据
- 处理缺失数据：DataFrame 可以包含缺失数据，并提供了多种方法来处理这些缺失值
- 数据操作：支持数据切片、索引‘子集分割等操作
- 时间序列支持：DataFrame 对时间序列数据有良好的支持，方便进行时间序列分析
- 灵活的数据处理功能：支持数据过滤、排序、分组、聚合等多种操作
- 数据导入导出：支持多种数据格式的导入和导出，如 CSV、Excel、SQL 等
- 滚动窗口和时间序列分析：支持对数据集进行滚动窗口计算和时间序列分析


2. 创建DataFrame
可以通过pandas.DataFrame()构造方法创建DataFrame：
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
- data：可以是多种数据结构，如字典、二维数组、Series、DataFrame或者其他可转为DataFrame对象，如果不提供则创建一个空的DataFrame
- index：行索引标签，可以是列表、数组、索引对象或其他可迭代对象，如果不提供则默认使用整数索引
- columns：列索引标签，可以是列表、数组、索引对象或其他可迭代对象，如果不提供则默认使用整数索引
- dtype：指定DataFrame中数据的类型，可以为Numpy中的数据类型，如果不提供则自动推断数据类型
- copy：布尔值，表示是否复制输入数据，默认为False，如果为True则复制数据


3. DataFrame的方法
(1) DataFrame.head(n)：返回DataFrame的前n行数据，默认n=5
(2) DataFrame.tail(n)：返回DataFrame的后n行数据，默认n=5
(3) DataFrame.info()：显示DataFrame的简要信息，包括索引、数据类型和内存使用情况等
(4) DataFrame.describe()：生成DataFrame数值列的统计信息，如计数、均值、标准差、最小值、四分位数和最大值等
(5) DataFrame.shape：返回DataFrame的维度信息，包含行数和列数
(6) DataFrame.columns：返回DataFrame的列标签
(7) DataFrame.index：返回DataFrame的行标签
(8) DataFrame.dtypes：返回DataFrame中每列的数据类型
(9) DataFrame.sort_values(by, axis=0, ascending=True)：根据指定列对DataFrame进行排序, ascending参数指定排序顺序
(10) DataFrame.sort_index(axis=0, ascending=True)：根据指定行对DataFrame进行排序, ascending参数指定排序顺序
(11) DataFrame.dropna()：删除包含缺失值的行或列
(12) DataFrame.fillna(value)：用指定的值填充缺失值
(13) DataFrame.isnull()：返回一个布尔型DataFrame，指示每个元素是否为缺失值
(14) DataFrame.notnull()：返回一个布尔型DataFrame，指示每个元素是否非缺失值
(15) DataFrame.loc[]：基于标签索引选择数据
(16) DataFrame.iloc[]：基于整数位置选择数据
(17) DataFrame.at[]：快速访问单个标量值，基于标签索引
(18) DataFrame.iat[]：快速访问单个标量值，基于整数位置
(19) DataFrame.apply(func, axis=0)：沿指定轴应用函数
(20) DataFrame.applymap(func)：对DataFrame中的每个元素应用函数
(21) DataFrame.groupby(by)：对DataFrame进行分组操作, 用于按某一列分组进行汇总统计
(22) DataFrame.pivot_table(values, index, columns, aggfunc='mean')：创建数据透视表
(23) DataFrame.merge(right, how='inner', on=None)：合并多个DataFrame
(24) DataFrame.concat(objs, axis=0)：按行或者按列连接多个DataFrame
(25) DataFrame.to_csv(path_or_buf, index=True)：将DataFrame导出为CSV文件
(26) DataFrame.to_excel(excel_writer, sheet_name='Sheet1', index=True)：将DataFrame导出为Excel文件
(27) DataFrame.to_json(path_or_buf, orient='records')：将DataFrame导出为JSON格式
(28) DataFrame.to_sql(name, con, if_exists='fail', index=True)：将DataFrame导出为SQL数据库表
(29) DataFrame.query(expr)：使用SQL表达式查询DataFrame中的数据
(30) DataFrame.duplicated()：返回一个布尔型DataFrame，指示每行是否为重复行
(31) DataFrame.drop_duplicates()：删除重复行
(32) DataFrame.set_index(keys)：设置DataFrame的行索引
(33) DataFrame.reset_index()：重置DataFrame的行索引
(34) DataFrame.transpose()：转置DataFrame，即行列互换
... 其他方法请参考Pandas官方文档。
"""
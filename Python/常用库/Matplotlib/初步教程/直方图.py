# Matplotlib 直方图

import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib提供了hist()函数来绘制直方图。
matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None,
                            cumulative=False, bottom=None, histtype='bar', align='mid',
                            orientation='vertical', rwidth=None, log=False, color=None,
                            label=None, stacked=False, **kwargs)[source]
- x：一维数组或列表，表示要绘制直方图的数据。
- bins：整数或序列，表示直方图的箱子数量。默认为10。
- range：元组，表示直方图的范围,默认为None，表示使用数据的最小值和最大值。
- density：布尔值，表示是否将直方图归一化为概率密度。默认为False。
- weights：一维数组或列表，表示每个数据点的权重。默认为None。
- cumulative：布尔值，表示是否绘制累计直方图。默认为False。
- bottom：浮点数或数组，表示直方图的底部位置。默认为None。
- histtype：字符串，表示直方图的类型。可选值有'bar'（默认值）、'barstacked'、'step'、'stepfilled'。
- align：字符串，表示直方图的对齐方式。可选值有'left'、'mid'（默认值）、'right'。
- orientation：字符串，表示直方图的方向。可选值有'vertical'（默认值）、'horizontal'。
- rwidth：浮点数，表示直方图的宽度比例。默认为None。
- log：布尔值，表示是否使用对数刻度。默认为False。
- color：字符串或数组，表示直方图的颜色。默认为None。
- label：字符串或数组，表示直方图的标签。默认为None。
- stacked：布尔值，表示是否绘制堆积直方图。默认为False。
- **kwargs：其他可选参数，用于设置直方图的属性，如边框颜色、线宽等。

显示图例：matplotlib.pyplot.legend(loc='best', **kwargs)
- loc：图例位置(可选，默认'best'，自动选择最佳位置)
- kwargs：其他参数(可选)
"""

# 实例1：基本直方图
data = np.random.randn(1000)
plt.hist(data, bins=30, color='blue', alpha=0.8)
plt.show()

# 实例2：绘制多组数据的直方图并比较
data1 = np.random.normal(0 , 1 , 1000)
data2 = np.random.normal(2 , 1.5 , 1000)
data3 = np.random.normal(-2 , 0.5 , 1000)

plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.hist(data3, bins=30, alpha=0.5, label='Data 3')
plt.legend() # 显示图例
plt.show()
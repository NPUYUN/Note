# Matplotlib 轴标签和标题

import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib 轴标签和标题

Matplotlib 图表的轴标签和标题是图表中最重要的元素之一。Matplotlib 提供了一些函数用于设置轴标签和标题。
1. 轴标签
可以使用matplotlib.pyplot.xlabel()和matplotlib.pyplot.ylabel()函数设置轴标签。

2. 标题
可以使用matplotlib.pyplot.title()函数设置标题。
"""

# 实例1：轴标签
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.plot(x, y)
plt.show()

# 实例2：标题
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.title('正弦函数')
plt.plot(x, y)
plt.show()
# Matplotlib 柱状图

import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib给出了bar()函数来绘制柱状图。
matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
- x: 包含x轴坐标的浮点数数组或元组。
- height: 包含每个柱的高度的浮点数数组或元组。
- width: 柱的宽度，默认为0.8。
- bottom: 柱的底部坐标，默认为0。
- align: 柱的对齐方式，可以是'center'(中心对齐)，'edge'(边缘对齐)，默认为'center'。
- data: 包含x轴坐标和高度的数组或DataFrame。
- **kwargs: 其他关键字参数，如color、edgecolor、hatch等。

垂直的柱状图改用barh()函数。其他的不变
"""

# 实例1：绘制简单的柱状图
x = np.arange(5)
y = np.random.randint(1, 10, 5)
plt.bar(x, y)
plt.show()

# 实例2：绘制垂直的柱状图
x = np.arange(5)
y = np.random.randint(1, 10, 5)
plt.barh(x, y)
plt.show()

# 实例3：设置柱状图颜色
x = np.arange(5)
y = np.random.randint(1, 10, 5)
plt.bar(x, y, color=['r', 'g', 'b', 'y', 'c'])
plt.show()

# 实例4：设置柱状图宽度和底部位置
x = np.arange(5)
y = np.random.randint(1, 10, 5)
plt.bar(x, y, width=0.5, bottom=2)
plt.show()
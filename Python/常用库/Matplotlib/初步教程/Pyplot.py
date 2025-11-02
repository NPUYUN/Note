# Matplotlib Pyplot

import matplotlib.pyplot as plt
import numpy as np

"""
Pyplot是Matplotlib的子库，提供了和MATLAB类似的绘图接口，能方便的绘制2D图表
Pyplot模块的基本函数有：
- plot()：绘制线图和散点图
- scatter()：绘制散点图
- bar()：绘制条形图
- hist()：绘制直方图
- imshow()：绘制图像
- subplot()：绘制子图
- show()：显示图表

下面介绍最简单的plot()函数用法：
(1) 画一条线
matplotlib.pyplot.plot([x], y, [fmt], data=None, **kwargs)
- x：横轴坐标数据(可选，若省略则默认从0开始到len(y)-1)
- y：纵轴坐标数据
- fmt：线条格式字符串(可选，默认'b-'，蓝色实线)
- data：数据(可选，若指定则x,y参数将被忽略)
- kwargs：其他参数(可选)

(2) 画多条线
matplotlib.pyplot.plot([x], y, [fmt], [x2], y2, [fmt2],..., **kwargs)
- x2, y2, fmt2：同上，绘制第二条线
- kwargs：其他参数(可选)
"""

# 实例1：普通线图
x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show() # 显示图表

# 实例2：设置标记符号
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])
plt.plot(a, b, 'o-') # 标记符号为圆点-
plt.show()

# 实例3：只传入纵轴坐标数据
y = np.array([1, 2, 3, 4, 5])
plt.plot(y)
plt.show()

# 实例4：绘制多条线
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.sin(x1)
x2 = np.array([2, 3, 4, 5, 6])
y2 = np.cos(x2)
plt.plot(x1, y1, x2 , y2)
plt.show()


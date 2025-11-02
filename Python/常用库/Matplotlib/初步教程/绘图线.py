# Matplotlib 绘图线

import matplotlib.pyplot as plt
import numpy as np

"""
绘图过程可以自定义线的样式、颜色和大小
1. 线的类型
线的类型可以使用linestyle(简写为ls)，包括：
- '-' 实线
- '--' 破折线
- '-.' 点划线
- ':' 虚线
- ''或' '：不画线

2. 线的颜色
线的颜色可以使用color(简写为c)，包括：
- 'r'：红色
- 'g'：绿色
- 'b'：蓝色
- 'y'：黄色
- 'k'：黑色
- 'w'：白色
- 'c'：青色
- 'm'：品红色
也包括HTML颜色代码，如'#FF0000'表示红色

3. 线的宽度
线的宽度可以使用linewidth(简写为lw)，单位为像素。

4. 多条线
如果要绘制多条线，可以用plot()函数一次绘制多条线，也可以用多次plot()函数绘制多条线。
"""

# 实例1：设置线的类型
x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y, ls='--')

# 实例2：设置线的颜色
x = np.arange(0, 10, 0.1)
y = np.cos(x)
plt.plot(x, y, c='r')

# 实例3：设置线的宽度
x = np.arange(0, 10, 0.1)
y = np.sin(x + 1)
plt.plot(x, y, lw=2)

# 实例4：绘制多条线
plt.show()

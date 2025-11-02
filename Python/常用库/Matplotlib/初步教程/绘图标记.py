# Matplotlib 绘图标记

import matplotlib.pyplot as plt
import numpy as np

"""
绘图过程如果想添加一些标记，比如图例、网格、坐标轴标签等，可以使用plot()方法的参数来定义
1. marker参数定义了标记的形状，有以下几种可选：
- '.' 点
- ',' 像素
- 'o' 圆圈
- 'v' 倒三角
- '^' 正三角
- '<' 左三角
- '>' 右三角
- '1' 下三叉
- '2' 上三叉
- '3' 左三叉
- '4' 右三叉
- '8' 八边形
- 's' 正方形
- 'p' 五边形
- ’P‘ 加号(填充)
- '*' 星号
- 'h' 六边形1
- 'H' 六边形2
- '+' 加号
- 'x' 乘号x
- 'X' 乘号x(填充)
- 'D' 菱形
- 'd' 瘦菱形
- '|' 竖线
- '_' 横线
- 0 左横线
- 1 右横线
- 2 上竖线
- 3 下竖线
- 4 左箭头
- 5 右箭头
- 6 上箭头
- 7 下箭头
- 8 左箭头(中间点为基准点)
- 9 右箭头(中间点为基准点)
- 10 上箭头(中间点为基准点)
- 11 下箭头(中间点为基准点)
- None 无标记
- '$...$' 渲染指定字符

2. fmt参数定义了基本格式，如标记、线条样式和颜色
fmt='[marker][line][color]'
(1) marker：标记，同上

(2) line：线条样式，有以下几种可选：
- '-' 实线
- '--' 破折线
- '-.' 点划线
- ':' 虚线

(3) color：颜色，有以下几种可选：
- 'b' 蓝色
- 'g' 绿色
- 'r' 红色
- 'c' 青色
- 'y' 黄色
- 'k' 黑色
- 'w' 白色
- ’m‘ 品红色

3. 标记的颜色和大小
定义标记的大小和颜色，使用的参数分别是
- markersize(简写ms)：标记大小
- markerfacecolor(简写mfc)：标记内部颜色
- markeredgecolor(简写mec)：标记边框颜色
"""

# 实例1：marker参数
x = np.linspace(0, 5, 10)
y = x**2
plt.plot(x, y, marker='o')
plt.show()

# 实例2：fmt参数
x = np.linspace(0, 5, 10)
y = x**2
plt.plot(x, y, 'r:o') # 红色虚线圆圈
plt.show()

# 实例3：设置标记大小和颜色参数
x = np.linspace(0, 5, 10)
y = x**2
plt.plot(x, y, 'r:o', markersize=10, markerfacecolor='w', markeredgecolor='r') # 红色虚线圆圈，大小为10，内部颜色为白色，边框颜色为红色
plt.show()


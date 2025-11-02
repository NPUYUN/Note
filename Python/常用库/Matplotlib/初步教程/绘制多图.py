# Matplotlib 绘制多图

import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib提供了subplot()和subplots()函数来绘制多个子图
1. subplot()函数
(1) matplotlib.pyplot.subplot(nrows, ncols, index, **kwargs)
- nrows：子图网格行数
- ncols：子图网格列数
- index：图的索引，从1开始，左上角为1，依次类推
- **kwargs：其他参数

(2) matplotlib.pyplot.subplot(pos, **kwargs)
- pos：子图的位置，如121，表示1行2列，第1个子图
- **kwargs：其他参数

(3) matplotlib.pyplot.subplot(**kwargs)
- **kwargs：其他参数

(4) matplotlib.pyplot.subplot(ax)
将已存在的轴对象作为子图添加到当前画布中
- ax：matplotlib.axes.Axes对象


2. subplots()函数
matplotlib.pyplot.subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
- nrows：子图网格行数
- ncols：子图网格列数
- sharex：x轴是否共享, 默认False(x轴独立), 可设置为'none'(x轴独立), True或'all'(所有子图共享x轴), 'row'(每个子图行共享一个x轴)、'col'(每个子图列共享一个x轴)
- sharey：y轴是否共享, 默认False(y轴独立), 可设置为'none'(y轴独立), True或'all'(所有子图共享y轴), 'row'(每个子图行共享一个y轴
- squeeze：是否压缩返回的轴对象, 默认True(当只有一个子图时返回单个轴对象), False(总是返回二维数组)
- subplot_kw：传递给每个子图的关键字参数字典
- gridspec_kw：传递给GridSpec构造函数的关键字参数字典
- **fig_kw：传递给Figure构造函数的关键字参数
"""

# 实例1：使用subplot()函数绘制多个子图
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Sine Wave')

plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.title('Sine Wave')

plt.subplot(223)
plt.plot(x, y)
plt.title('Sine Wave')

plt.subplot(224)
plt.plot(x, y)
plt.title('Sine Wave')

plt.suptitle('Multiple Subplots')
plt.show()

# 实例2：使用subplots()函数绘制多个子图
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# 创建一个画像和一个子图
fig, axes = plt.subplots()
axes.plot(x, y)
axes.set_title('Sine Wave')

# 创建两个子图
f, (ax1, ax2) = plt.subplots(1 , 2)
ax1.plot(x, y, 'tab:blue')
ax1.set_title('Sine Wave 1')
ax2.plot(x, -y, 'tab:orange')
ax2.set_title('Sine Wave 2')

# 创建四个子图
f, axs = plt.subplots(2, 2, subplot_kw={'projection': 'polar'})
axs[0, 0].plot(x, y)
axs[1 ,1].plot(x, -y)

# 共享x轴
plt.subplots(2, 2, sharex='col')

# 共享y轴
plt.subplots(2, 2, sharey='row')

# 共享x轴和y轴
plt.subplots(2, 2, sharex='all', sharey='all')

# 创建标识为10的子图，存在则删除
plt.subplots(num=10, clear=True)

plt.show()


#

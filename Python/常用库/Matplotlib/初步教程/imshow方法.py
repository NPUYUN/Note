# Matplotlib imshow方法

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

"""
imshow()函数是Matplotlib库中用于显示图像数据的函数。它可以将二维数组表示为图像
imshow()函数常用于绘制二维的灰度图像和彩色图像，例如绘制矩阵、热图等。

matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None, 
                        interpolation=None, alpha=None, vmin=None, 
                        vmax=None, origin=None, extent=None, filternorm=1, 
                        filterrad=4.0, imlim=None, resample=None, url=None, data=None, **kwargs)
- X: 要显示的二维数组、三维数组、图像数据、matplotlib路径对象、PIL图像对象等。
- cmap: 用于映射数据值到颜色的Colormap对象。
- norm: 用于归一化数据的Normalize对象。
- aspect: 图像的纵横比，可以是'auto'、'equal'或一个数值。
- interpolation: 插值方法，用于调整图像的显示效果，如'nearest'、'bilinear'等。
- alpha: 图像的透明度，取值范围为0（完全透明）到1（完全不透明）。
- vmin和vmax: 用于设置数据值的最小值和最大值，以控制颜色映射的范围。
- origin: 图像的原点位置，可以是'upper'（默认）或'lower'。
- extent: 图像的边界范围，格式为[xmin, xmax, ymin, ymax]。
- filternorm和filterrad: 用于控制图像滤波的参数，可以设置为None、antigrain、freetype等
- imlim: 图像的显示限制。
- resample: 是否对图像进行重采样。
- url: 图像的URL链接。
- data: 传递给函数的数据。
- **kwargs: 其他可选参数，如标签、标题等。
"""

# 实例1：显示灰度图像
img = np.random.rand(10 , 10)
plt.imshow(img, cmap='gray')
plt.colorbar()
plt.show()

# 实例2：显示彩色图像
img = np.random.rand(10, 10, 3)
plt.imshow(img) # 彩色图像不需要指定cmap
plt.show()

# 实例3：显示热力图
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot')
plt.colorbar()
plt.show()

# 实例4：显示地图
img = Image.open('map.jpeg')  # 替换为实际的地图图像路径
data = np.array(img)
plt.imshow(data)
plt.axis('off')  # 关闭坐标轴显示
plt.show()

# 实例5：显示矩阵
data = np.random.rand(10 , 10)
plt.imshow(data)
plt.show()

# 实例6：使用插值
data = np.reshape(np.linspace(0 , 1 , 4**2) , (4 , 4))
plt.imshow(data, cmap='viridis', interpolation='nearest') # 最近邻插值
plt.colorbar()
plt.show()
plt.imshow(data, cmap='viridis', interpolation='bicubic') # 双三次插值
plt.colorbar()
plt.show()
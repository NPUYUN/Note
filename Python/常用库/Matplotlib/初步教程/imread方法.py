# Matplotlib imread方法

import matplotlib.pyplot as plt
import numpy as np

"""
imread方法用于读取图像文件并将其加载为NumPy数组。形状为(nrows, ncols, nchannels)。
- nrows: 图像的高度（行数）。
- ncols: 图像的宽度（列数）。
- nchannels: 图像的通道数（灰度图像为1，彩色图像为3或4，分别包括红(0)、绿(1)、蓝(2)以及alpha通道）。

matplotlib.pyplot.imread(fname, format=None)
- fname: 要读取的图像文件名，可以包含路径和扩展名。
- format: 可选参数，指定图像格式（如'png'、'jpeg'等），通常不需要指定，Matplotlib会根据文件扩展名自动识别格式
"""

# 实例1：读取并显示图像
img = plt.imread('map.jpeg')
plt.imshow(img)
plt.show()

# 实例2：图像变暗
img = plt.imread('map.jpeg')
m = img/255 # 归一化到0-1之间
for i in range(1 , 5):
    plt.subplot(2, 2, i)
    plt.imshow(m* i * 0.2) # 变暗处理
plt.show()

# 实例3：裁剪图像
img = plt.imread('map.jpeg')
plt.imshow(img[100:400, 200:500]) # 裁剪部分图像
plt.show()

# 实例4：调整图像颜色
img = plt.imread('map.jpeg')
red_map = img.copy()
red_map[:, :, [1, 2]] = 0 # 去掉绿色通道和蓝色通道
plt.imshow(red_map)
plt.show()
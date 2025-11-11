# Matplotlib imsave方法

import matplotlib.pyplot as plt
import numpy as np

"""
imsave方法用于将图像数据保存为图像文件，如PNG、JPEG等。
matplotlib.pyplot.imsave(fname, arr, **kwargs)
- fname: 保存的文件名，可以包含路径和扩展名。
- arr: 要保存的图像数据，通常是一个二维或三维的NumPy数组。
- **kwargs: 其他可选参数，如cmap（颜色映射）、vmin、vmax等。
"""

# 实例：保存一个简单的二维数组
data = np.random.rand(100, 100, 3) # 生成一个100x100的随机RGB图像

plt.imsave('random_image.png', data) # 没有指定图像格式，保存为PNG
plt.imsave('random_image.jpg', data) # 没有指定图像格式，保存为JPEG
plt.imsave('random_image_cmap.png', data, cmap='gray') # 使用颜色映射保存图像


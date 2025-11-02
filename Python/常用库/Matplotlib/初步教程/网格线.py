# Matplotlib 网格线

import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib网格线可以通过pyplot.grid()方法来设置：
plt.grid(b=None, which='major', axis='both', **kwargs)
- b: 是否显示网格线，True为显示，False为不显示，默认值为None，表示根据其他参数设置决定是否显示网格线。
- which: 网格线类型，'major'为主网格线，'minor'为次网格线，默认值为'major'。
- axis: 网格线所在轴，'both'为两轴，'x'为x轴，'y'为y轴，默认值为'both'。
- **kwargs: 其他参数，如颜色、线宽、样式等。
"""

# 实例1：直接添加网格线
plt.plot(np.random.rand(10))
plt.grid(True)
plt.show()

# 实例2：只显示x轴网格线
plt.plot(np.random.rand(10))
plt.grid(True, axis='x')
plt.show()

# 实例3：设置网格线颜色、线宽、样式
plt.plot(np.random.rand(10))
plt.grid(True, axis='both', c='r', lw=0.5, ls='-.')
plt.show()


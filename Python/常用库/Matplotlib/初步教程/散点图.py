# Matplotlib 散点图

import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib提供了scatter()函数来绘制散点图。
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None, plotnonfinite=False, **kwargs)
- x，y：长度相同的数组，表示散点的坐标。
- s：散点的大小，可以是单个数值或每个散点大小的数组。默认为20。
- c：散点的颜色，可以是单个颜色值或每个散点颜色的数组。默认为蓝色。
- marker：散点的形状，默认为'o'。
- cmap：颜色映射，用于根据数值映射颜色。默认为None。为标量或者一个colormap名字，只有c是一个浮点数数组时才能使用，如果没有申明就是image.cmap。
- norm：归一化，用于缩放颜色映射。默认为None。为一个Normalize实例，只有c是一个浮点数数组时才能使用。
- vmin，vmax：亮度。默认为None。在norm参数存在时忽略
- alpha：散点的透明度，取值范围为0到1。默认为None.即完全不透明。
- linewidths：标记点的长度
- edgecolors：颜色或者颜色序列，用于设置散点边缘的颜色。默认为'face'，可选值有'face'，'none'或者颜色序列。
- plotnonfinite：是否绘制非有限值（如NaN或Inf）。默认为False。
- **kwargs：其他可选参数，如标签、zorder等。


颜色条Colormap
颜色条就像是一个颜色列表，其中每种颜色都有一个范围为0到100的值
设置颜色条需要使用cmap参数，可以使用Matplotlib内置的颜色映射名称，如'viridis'(默认)、'plasma'、'inferno'、'magma'等。
显示颜色条可以使用plt.colorbar()函数。

颜色条的设置可以为：
- Accent(Accent, Accent_r)：浅蓝色到深蓝色，适用于有色调的图表
- Blues(Blues, Blues_r)：浅蓝色到深蓝色，适用于无色调的图表
- BrBG(BrBG, BrBG_r)：青色到浅黄色，适用于有色调的图表
- BuGn(BuGn, BuGn_r)：浅绿色到深绿色，适用于有色调的图表
- BuPu(BuPu, BuPu_r)：浅紫色到深紫色，适用于有色调的图表
- CMRmap(CMRmap, CMRmap_r)：浅蓝色到深黄色，适用于有色调的图表
- Dark2(Dark2, Dark2_r)：深蓝色到浅蓝色，适用于有色调的图表
- GnBu(GnBu, GnBu_r)：浅蓝色到深绿色，适用于有色调的图表
- Greens(Greens, Greens_r)：浅绿色到深绿色，适用于无色调的图表
- Greys(Greys, Greys_r)：浅灰色到深灰色，适用于无色调的图表
- OrRd(OrRd, OrRd_r)：浅红色到深红色，适用于有色调的图表
- Oranges(Oranges, Oranges_r)：浅橙色到深橙色，适用于无色调的图表
- PRGn(PRGn, PRGn_r)：浅蓝色到深绿色，适用于有色调的图表
- Paired(Paired, Paired_r)：一组配对的颜色，适用于有色调的图表
- Pastel1(Pastel1, Pastel1_r)：一组有点粉的颜色，适用于有色调的图表
- Pastel2(Pastel2, Pastel2_r)：一组有点粉的颜色，适用于有色调的图表
- PiYG(PiYG, PiYG_r)：浅蓝色到深黄色，适用于有色调的图表
- PuBu(PuBu, PuBu_r)：浅蓝色到深紫色，适用于有色调的图表
- PuBuGn(PuBuGn, PuBuGn_r)：浅蓝色到深绿色，适用于有色调的图表
- PuOr(PuOr, PuOr_r)：浅蓝色到深橙色，适用于有色调的图表
- PuRd(PuRd, PuRd_r)：浅紫色到深红色，适用于有色调的图表
- Purples(Purples, Purples_r)：浅紫色到深紫色，适用于无色调的图表
- RdBu(RdBu, RdBu_r)：浅红色到深蓝色，适用于有色调的图表
- RdGy(RdGy, RdGy_r)：浅红色到深灰色，适用于有色调的图表
- RdPu(RdPu, RdPu_r)：浅紫色到深红色，适用于有色调的图表
- RdYlBu(RdYlBu, RdYlBu_r)：浅蓝色到深黄色，适用于有色调的图表
- RdYlGn(RdYlGn, RdYlGn_r)：浅蓝色到深绿色，适用于有色调的图表
- Set1(Set1, Set1_r)：一组有序的颜色，适用于有色调的图表
- Set2(Set2, Set2_r)：一组有序的颜色，适用于有色调的图表
- Set3(Set3, Set3_r)：一组有序的颜色，适用于有色调的图表
- Spectral(Spectral, Spectral_r)：浅蓝色到深黄色，适用于有色调的图表
- Wistia(Wistia, Wistia_r)：浅紫色到深紫色，适用于有色调的图表
- YlGn(YlGn, YlGn_r)：浅绿色到深蓝色，适用于有色调的图表
- YlGnBu(YlGnBu, YlGnBu_r)：浅绿色到深蓝色，适用于有色调的图表
- YlOrBr(YlOrBr, YlOrBr_r)：浅橙色到深红色，适用于有色调的图表
- YlOrRd(YlOrRd, YlOrRd_r)：浅橙色到深红色，适用于有色调的图表
"""

# 实例1：普通的散点图
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.show()

# 实例2：设置散点大小
x = np.random.rand(100)
y = np.random.rand(100)
s = np.random.rand(100) * 100
plt.scatter(x, y, s=s)
plt.show()

# 实例3：设置散点颜色
x = np.random.rand(100)
y = np.random.rand(100)
c = np.random.rand(100)
plt.scatter(x, y, c=c)
plt.show()

# 实例4：设置两组散点图
x1 = np.random.rand(50)
y1 = np.random.rand(50)
x2 = np.random.rand(50)
y2 = np.random.rand(50)
plt.scatter(x1, y1, c='r', marker='o')
plt.scatter(x2, y2, c='b', marker='^')
plt.show()

# 实例5：使用颜色映射和颜色条
x = np.random.rand(100)
y = np.random.rand(100)
c = np.random.rand(100)
plt.scatter(x, y, c=c, cmap='viridis')
plt.colorbar()
plt.show()
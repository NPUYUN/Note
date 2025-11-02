# Matplotlib 饼图

import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib提供了pie()函数来绘制饼图。
matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None,
                      pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None,
                      radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, data=None)[source]
- x：浮点数数组或列表，用于绘制饼图的数据。
- explode：数组，表示各个扇形之间的偏移量。默认为0
- labels：用于为每个部分添加标签的数组或列表，默认为None
- colors：用于指定每个部分颜色的数组或列表，默认为None
- autopct：字符串格式，用于显示每个部分的百分比。默认为None，%d%%表示整数百分比，%.1f%%表示一位小数百分比
- pctdistance：浮点数，表示百分比标签与圆心的距离比例，默认为0.6
- shadow：布尔值，表示是否为饼图添加阴影效果，默认为False
- labeldistance：浮点数，表示标签与圆心的距离比例，默认为1.1
- startangle：浮点数，表示饼图起始角度，默认为None，表示从x轴正方向开始绘制
- radius：浮点数，表示饼图的半径，默认为1
- counterclock：布尔值，表示是否逆时针绘制饼图，默认为True
- wedgeprops：字典，表示扇形的属性，如边框颜色、线宽等，默认为None
- textprops：字典，表示文本标签的属性，如字体大小、颜色等，默认为None
- center：元组，表示饼图的中心位置，默认为(0, 0)
- frame：布尔值，表示是否绘制饼图的边框，默认为False
- rotatelabels：布尔值，表示是否旋转标签以适应扇形，默认为False
- data：用于传递数据源，如果指定了data参数，可以直接在x、labels等参数中使用data中的列名进行引用，默认为None
除此之外，pie()函数还可以返回三个值：
- wedges：表示饼图中各个扇形的对象列表
- texts：表示饼图中各个标签的文本对象列表
- autotexts：表示饼图中自动生成的文本标签对象列表      
"""

# 实例1：基本饼图
y = np.array([30, 20, 45, 5])
plt.pie(y)
plt.show()

# 实例2：设置饼图各个扇形的标签和颜色
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'blue', 'green', 'yellow']
plt.pie(y, labels=labels, colors=colors)
plt.show()

# 实例3：设置饼图各个扇形的偏移量和百分比显示，并添加阴影效果
explode = [0.1, 0, 0, 0]
plt.pie(y, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True)
plt.show()
# NumPy IO

import numpy as np

"""
Numpy 可以读写磁盘上的文件，包括文本文件和二进制文件。
NumPy 为ndarray对象引入了一个简单的文件格式，称为.npy。
.npy 文件可以保存数组数据，并在需要时轻松地加载。

常用的IO函数：
(1) numpy.save(file, arr, allow_pickle=True, fix_imports=True)
将数组 arr 保存到文件 file 中，以.npy 格式。
- file：文件名或文件对象。
- arr：要保存的数组。
- allow_pickle：如果为 True，则允许保存对象数组。
- fix_imports：如果为 True，则在导入模块时修复 __import__ 语句。

(2) numpy.savez(file, *args, **kwds)
将多个数组保存到一个.npz 文件中。
- file：文件名或文件对象。
- args：要保存的数组。
- kwds：要保存的关键字参数。

(3) numpy.savetxt(file, arr, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')
将数组 X 保存到文件 file 中，以文本格式。
- file：文件名或文件对象。
- arr：要保存的数组。
- fmt：格式字符串。
- delimiter：分隔符。
- newline：换行符。
- header：文件头。
- footer：文件尾。
- comments：注释符。

(4) numpy.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
从文件 file 中加载数组。
- file：文件名或文件对象。
- mmap_mode：内存映射模式。
- allow_pickle：如果为 True，则允许加载对象数组。
- fix_imports：如果为 True，则在导入模块时修复 __import__ 语句。
- encoding：编码格式。

(5) numpy.loadtxt(fname, dtype=float, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
从文件 fname 中加载数组。
- fname：文件名或文件对象。
- dtype：数据类型。
- comments：注释符。
- delimiter：分隔符。
- converters：转换器。
- skiprows：跳过的行数。
- usecols：要使用的列。
- unpack：是否解包。
- ndmin：最小维度。

(6) numpy.genfromtxt(fname, dtype=float, comments='#', delimiter=None, skip_header=0, skip_footer=0, converters=None, missing_values=None, filling_values=nan, usecols=None, names=None, excludelist=None, deletechars=None, replace_space='_', autostrip=False, case_sensitive=True, defaultfmt='f%i', unpack=None, usemask=False, loose=True, invalid_raise=True)
从文件 fname 中加载数组,处理缺失值。
- fname：文件名或文件对象。
- dtype：数据类型。
- comments：注释符。
- delimiter：分隔符。
- skip_header：跳过的行数。
- skip_footer：跳过的行数。
- converters：转换器。
- missing_values：缺失值。
- filling_values：填充值。
- usecols：要使用的列。
- names：列名。
- excludelist：要排除的列。
- deletechars：要删除的字符。
- replace_space：替换空格符。
- autostrip：是否自动去除空白符。
- case_sensitive：是否大小写敏感。
- defaultfmt：默认格式。
- unpack：是否解包。
- usemask：是否使用掩码。
- loose：是否宽松模式。
- invalid_raise：是否抛出异常。
"""

# 实例1：保存数组到文件
a = np.array([[1, 2, 3], [4, 5, 6]])
np.save('test.npy', a)

# 实例2：保存多个数组到文件
b = np.array([1, 2, 3])
c = np.array([4, 5, 6])
np.savez('test.npz', a, b, c)

# 实例3：保存数组到文本文件
d = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('test.txt', d, fmt='%d', delimiter=' ')

# 实例4：加载数组
e = np.load('test.npy')
print(e)

# 实例5：加载文本文件
f = np.loadtxt('test.txt', dtype=int, delimiter=' ')
print(f)
# Numpy 迭代数组
import numpy as np

"""
Numpy的迭代器对象numpy.nditer()提供了一种灵活访问一个或者多个数组元素的方式
1. 对数组元素的访问
和python的迭代器对象一样，numpy.nditer()可以用来访问数组元素。
即for i in numpy.nditer(arr):
tips：a.T表示a的转置

2. 控制遍历顺序
可以使用numpy.nditer()的order参数来控制遍历顺序。
访问顺序的差异：
- C：行优先，从左到右
- F：列优先，从上到下
- A：自动选择，由numpy决定，一般情况下，C访问速度更快。

3. 修改数组中元素的值
numpy.nditer()有一个可选参数op_flags，默认为只读对象(['read-only'])，为了修改值，必须指定为readwrite或者writeonly。
然后使用x[...] = value来修改数组元素的值。
注意：直接对a[]修改较为繁琐，故采用对x[...]赋值的方式。x[...]的用法类似于python的切片操作。
x[...]表示原数组中遍历到的个体元素，x表示遍历到的个体元素，x[...] = value表示将目前遍历到的元素更新成value，会直接修改原数组的值。
注：op_flags=[('权限1','权限2',...,)]可以指定多个操作权限，具体有：
- readwrite：可读可写
- readonly：只读
- writeonly：只写
- copy：在迭代的时候创建副本，而不是修改原数组
- no-broadcast：不允许广播

4. 使用外部循环
numpy.nditer()中有flags=['']参数，可以接受以下参数
- c_index：可以跟踪C顺序的索引，即可以获取当前元素的索引(nditer对象.index)
- f_index：可以跟踪F顺序的索引，即可以获取当前元素的索引(nditer对象.index)
- multi_index：每次迭代可以跟踪一种索引类型，当数组是多维的时候使用，在迭代过程中可以获取到当前元素的多维索引
- external_loop：给出的值是具有多个值的一维数组，而不是零维数组，即将每次迭代一个一维数组

5. 广播迭代
如果两个数组是可广播的，nditer可以同时迭代他们，并且会自动进行广播。
"""

# 实例1：访问数组元素
a = np.arange(6).reshape(2 , 3)
for x in np.nditer(a):
    print(x , end=',')
print()

# 实例2：修改遍历顺序
# 方式1：设置nditer里的order参数
a = np.arange(6).reshape(2, 3)
for x in np.nditer(a, order='F'):
    print(x , end=',')
print()
# 方式2：使用arr.copy中的order参数修改存储顺序
for x in np.nditer(a.copy(order='F')):
    print(x , end=',')
print()

# 实例3：修改数组元素的值
a = np.arange(6).reshape(2, 3)
for x in np.nditer(a , op_flags=[('readwrite',)]):
    x[...] = 2 * x # 每个元素乘以2
print(a)

# 实例4：使用外部循环
a = np.arange(6).reshape(2, 3)
for x in np.nditer(a, flags=['external_loop']):
    print(x , end=',')
it = np.nditer(a, flags=['c_index'])
for x in it:
    print(it.index, end=',') # 通过it.index获取当前元素的索引






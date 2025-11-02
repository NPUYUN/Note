# Numpy 字符串函数

import numpy as np
"""
Numpy提供了对于dtype为numpy.string_或者numpy.unicode_的数组的一些字符串处理函数。
这些函数在字符数组类(numpy.char)中定义：
1. add(arr1, arr2)：对两个字符串数组的逐个元素进行连接，返回一个新的字符串数组。
- arr1、arr2：输入的字符串数组，形状兼容

2. multiply(arr, n)：对字符串数组的每个元素重复n次，返回一个新的字符串数组。
- arr：输入的字符串数组
- n：重复次数

3. center(arr, width, fillchar=' ')：将字符串数组的每个元素居中，总长度为width，不足部分用fillchar填充，返回一个新的字符串数组。
- arr：输入的字符串数组
- width：目标字符串长度
- fillchar：填充字符，默认为空格

4. capitalize(arr)：将字符串数组的每个元素的首字母大写，其余字母小写，返回一个新的字符串数组。
- arr：输入的字符串数组

5. title(arr)：将字符串数组的每个元素的每个单词的首字母大写，其余字母小写，返回一个新的字符串数组。
- arr：输入的字符串数组

6. lower(arr)：将字符串数组的每个元素转换为小写，返回一个新的字符串数组。
- arr：输入的字符串数组

7. upper(arr)：将字符串数组的每个元素转换为大写，返回一个新的字符串数组。
- arr：输入的字符串数组

8. split(arr, sep=None, maxsplit=-1)：将字符串数组按照sep分割maxsplit次(-1表示无限制)，返回一个数组列表。
- arr：输入的字符串数组
- sep：分隔符，默认为空格
- maxsplit：最大分割次数，默认-1

9. splitlines(arr, keepends=False)：将字符串数组按照换行符分割，返回一个数组列表。
- arr：输入的字符串数组
- keepends：是否保留换行符，默认False

10. strip(arr, chars=None)：去除字符串数组中吗每个元素两端的特定字符，返回一个新的字符串数组。
- arr：输入的字符串数组
- chars：要去除的字符，默认为空格

11. join(sep, arr)：用分隔符sep连接字符串数组的元素中每一个字符，返回一个新的字符串数组。
- sep：分隔符
- arr：输入的字符串数组

12. replace(arr, old, new, count=-1)：将字符串数组中old替换为new，count表示替换次数(-1表示全部替换)，返回一个新的字符串数组。
- arr：输入的字符串数组
- old：要被替换的子串
- new：新子串
- count：替换次数，默认-1

13. decode(arr, encoding=None, errors=None)：对字节数组(numpy.string_)执行str.decode操作，实现解码，返回一个新的字符串数组。
- arr：输入的字节数组
- encoding：编码格式，默认None
- errors：错误处理方式，默认None

14. encode(arr, encoding=None, errors=None)：对字符串数组(numpy.unicode_)执行str.encode操作，实现编码，返回一个新的字节数组(numpy.string_).
- arr：输入的字符串数组
- encoding：编码格式，默认None
- errors：错误处理方式，默认None
"""

# 实例1：add(arr1, arr2)
a = np.array(['hello ', 'world '])
b = np.array(['numpy', 'tutorial'])
c = np.char.add(a, b)
print(c)

# 实例2：multiply(arr, n)
a = np.array(['hello ', 'world '])
b = np.char.multiply(a, 3)
print(b)

# 实例3：center(arr, width, fillchar=' ')
a = np.array(['hEllo', 'world'])
b = np.char.center(a, 10, fillchar='*')
print(b)

# 实例4：capitalize(arr)
a = np.array(['hello', 'world'])
b = np.char.capitalize(a)
print(b)

# 实例5：title(arr)
a = np.array(['hello world', 'numpy tutorial'])
b = np.char.title(a)
print(b)

# 实例6：lower(arr)
a = np.array('HELLO')
b = np.char.lower(a)
print(b)

# 实例7：upper(arr)
a = np.array('hello')
b = np.char.upper(a)
print(b)

# 实例8：split(arr, sep=None, maxsplit=-1)
a = np.array(['hello world', 'numpy tutorial'])
b = np.char.split(a, sep=' ')
print(b)

# 实例9：splitlines(arr, keepends=False)
a = np.array(['hello\nworld', 'numpy\ntutorial'])
b = np.char.splitlines(a)
print(b)

# 实例10：strip(arr, chars=None)
a = np.array(['  hello  ', 'world  '])
b = np.char.strip(a)
print(b)

# 实例11：join(sep, arr)
a = np.array(['hello', 'world'])
b = np.char.join(['-' , ':'], a)
print(b)

# 实例12：replace(arr, old, new, count=-1)
a = np.array(['hello world', 'numpy tutorial'])
b = np.char.replace(a, 'o', '0', count=1)
print(b)

# 实例13：decode(arr, encoding=None, errors=None)
a = np.array([b'hello', b'world']) # 字节数组
b = np.char.decode(a) # 解码为字符串数组
print(b)

# 实例14：encode(arr, encoding=None, errors=None)
a = np.array(['hello', 'world']) # 字符串数组
b = np.char.encode(a) # 编码为字节数组
print(b)
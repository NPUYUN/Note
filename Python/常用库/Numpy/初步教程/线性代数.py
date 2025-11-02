# Numpy 线性代数

import numpy as np

"""
Numpy提供了线性代数函数库linalg，包括了线性代数所需要的全部功能，包括：
1. 基础矩阵的运算
(1) numpy.linalg.dot(x1, x2, out=None)
计算两个数组的点积
- x1 , x2：两个维度相同数组且符合点积规则
- out : 输出数组，用于存储结果的输出数组
注意：
对于两个一维数组，点积等价于内积
其余情况，点积等价于矩阵乘积

(2) numpy.linalg.vdot(x1, x2)
计算两个向量的共轭点积
- x1 , x2 : 两个向量，维度相同，且符合点积规则
- out : 输出数组，用于存储结果的输出数组
计算逻辑：先将多维数组展平成1维向量，对第二个参数取共轭复数，再计算乘积和

(3) numpy.linalg.inner(x1, x2, out=None)
计算两个数组的内积
- x1 , x2 : 两个数组，维度相同，且符合内积规则
- out : 输出数组，用于存储结果的输出数组

(4) numpy.linalg.matmul(x1, x2, out=None)
计算两个矩阵的乘积
- x1 , x2 : 两个矩阵，注意形状必须符合对应规则且为二维及以上数组
- out : 输出矩阵，用于存储结果的输出数组

(5) numpy.linalg.det(a)
计算方阵的行列式
- a : 一个方阵，维度为n*n

(6) numpy.linalg.inv(a)
计算方阵的逆矩阵
- a : 一个方阵，维度为n*n

2. 线性方程组的求解
(1) numpy.linalg.solve(a, b)
求解线性方程组Ax = b
- a：方阵
- b：右端常数

(2) numpy.linalg.lstsq(a, b, rcond=None)
求解超定方程组的最小二乘解
- a：方阵
- b：右端常数
- rcond：奇异值阈值，默认为1e-15
返回解、残差、秩、剩余奇异值


3. 矩阵分解
(1) numpy.linalg.eig(a)
求解方阵a的特征值和特征向量
- a：方阵

(2) numpy.linalg.eigh(a)
求解方阵a的特征值和特征向量，只适用于Hermitian矩阵
- a：对称方阵

(3) numpy.linalg.svd(a, full_matrices=True, compute_uv=True)
求解矩阵a的奇异值分解
- a：矩阵
- full_matrices：是否返回完整矩阵
- compute_uv：是否计算U和V
返回：
- U：左奇异矩阵
- s：奇异值
- V：右奇异矩阵的转置

(4) numpy.linalg.QR(a, mode='reduced')
求解矩阵a的QR分解(正交矩阵Q和上三角矩阵R)
- a：矩阵
- mode：'reduced'，'complete'，

(5) numpy.linalg.cholesky(a)
求解矩阵a的Cholesky分解(将矩阵A分解为L-L^T，L为下三角矩阵)
- a：对称正定矩阵

3. 范数与条件数
(1) numpy.linalg.norm(x, ord=None, axis=None, keepdims=False)
计算矩阵的范数
- x：向量或矩阵
- ord：范数类型，可以是'fro'，'nuc'，'inf'，'1'，'2'，'np.inf'，'None'
- axis：计算范数的轴，可以是None，0，1，-1
- keepdims：是否保持维度

(2) numpy.linalg.cond(x, p=None)
计算矩阵的条件数(衡量病态程度)
- x：矩阵
- p：计算条件数的阶数(范数类型)，默认为2

4. 其他
(1) numpy.linalg.matrix_rank(a, tol=None)
计算矩阵a的秩
- a：矩阵
- tol：奇异值阈值，默认为1e-12

(2) numpy.linalg.pinv(a, rcond=1e-15)
计算矩阵a的Moore-Penrose伪逆矩阵
- a：矩阵
- rcond：奇异值阈值，默认为1e-15

(3) numpy.linalg.tensorinv(a, ind=2)
计算张量a的逆矩阵
- a：张量
- ind：张量的阶数，默认为2

(4) numpy.linalg.kron(a, b)
计算两个矩阵的Kronecker积(两个矩阵的笛卡尔积的乘积)
- a：矩阵
- b：矩阵
"""

# 实例1：矩阵乘法
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
print(c)
d = np.vdot(a, b)
print(d)
e = np.inner(a, b)
print(e)
f = np.matmul(a, b)
print(f)

# 实例2：矩阵求行列式
a = np.array([[1, 2], [3, 4]])
d = np.linalg.det(a)
print(int(d))

# 实例3：矩阵求逆
a = np.array([[1, 2], [3, 4]])
b = np.linalg.inv(a)
print(b)

# 实例4：线性方程组求解
a = np.array([[3, 2], [2, 4]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)
print(x)

# 实例5：超定方程组求解
a = np.array([[1, 2], [2, 4], [3, 6]])
b = np.array([1, 2, 3])
x, residuals, rank, s = np.linalg.lstsq(a, b, rcond=None)
print(x)
print(residuals)
print(rank)
print(s)

# 实例6：求矩阵的特征值和特征向量
a = np.array([[1, 2], [3, 4]])
w, v = np.linalg.eig(a)
print(w)
print(v)

# 实例7：求对称矩阵的特征值和特征向量
a = np.array([[1, 2], [2, 4]])
w, v = np.linalg.eigh(a)
print(w)
print(v)

# 实例8：奇异值分解
a = np.array([[1, 2], [3, 4]])
u, s, vh = np.linalg.svd(a, full_matrices=True, compute_uv=True)
print(u)
print(s)
print(vh)

# 实例9：QR分解
a = np.array([[1, 2], [3, 4]])
q, r = np.linalg.qr(a, mode='reduced')
print(q)
print(r)

# 实例10：Cholesky分解
a = np.array([[1, 0], [0, 1]])
l = np.linalg.cholesky(a)
print(l)

# 实例11：范数计算
a = np.array([[1, 2], [3, 4]])
b = np.linalg.norm(a)
print(b)

# 实例12：条件数计算
a = np.array([[1, 2], [3, 4]])
b = np.linalg.cond(a)
print(b)

# 实例13：矩阵秩计算
a = np.array([[1, 2], [3, 4]])
b = np.linalg.matrix_rank(a)
print(b)
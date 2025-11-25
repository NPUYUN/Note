from scipy.optimize import linprog
import pulp
import cvxpy as cp

"""
线性规划：
(1)定义：在一组线性约束条件的限制下，求一线性目标函数最大或最小的问题
(2)三要素：
(2.1)决策变量：待优化的变量
(2.2)目标函数：需要最大化或最小化的函数
(2.3)约束条件：限制决策变量取值的条件

Python求解线性规划有三种途径
1. scipy.optimize.linprog
Scipy的linprog函数默认求解最小化问题，因此需将目标函数系数取负号，将约束条件系数取正号

2. pulp
3. cvxpy
"""
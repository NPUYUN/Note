"""
模型构建
1. 决策变量：x1，x2，x3分别代表第一、二、三季度的产量

2. 目标函数：最小化总成本(生成成本+仓储费用)
(1) 每个季度的生产成本为f(x) = ax + bx**2
(2) 仓储费：4(3x1 + 2x2 + x3 - 320)
第一季度：I1 = x1 - 40
第二季度：I2 = x1 + x2 - 100
第三季度：I3 = x1 + x2 + x3 - 180
(3) 目标函数：z = 0.5(x1**2 + x2**2 + x3**2) + 62x1 + 58x2 + 54x3 - 1280

3. 约束条件
(1) 交货要求库存非负：x1 >= 40   x1 + x2 >= 100  x1 + x2 + x3 >= 180
(2) 生产能力限制：x1 <= 100   x2 <= 100   x3 <= 100
"""

from scipy.optimize import minimize
import numpy as np

def objective_function(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    I1 = x1 - 40
    I2 = x1 + x2 - 100
    I3 = x1 + x2 + x3 - 180
    return 0.5 * (x1**2 + x2**2 + x3**2) + 50 * (x1 + x2 + x3) - 4 * (I1 + I2 + I3)

def constraint_function1(x):
    return x[0] - 40

def constraint_function2(x):
    return x[0] + x[1] - 100

def constraint_function3(x):
    return x[0] + x[1] + x[2] - 180

constraints = [
    {'type': 'ineq' , 'fun': constraint_function1},
    {'type': 'ineq' , 'fun': constraint_function2},
    {'type': 'ineq' , 'fun': constraint_function3},
]

x0 = np.array([0 , 0 , 0])

result = minimize(objective_function ,  x0 , constraints = constraints , bounds=[(0 , 100) , (0 , 100) , (0 , 100)])

print("最优解：" , result.x)
print("目标函数值：" , result.fun)
print("迭代次数：" , result.nit)
print("是否收敛：" , result.success)

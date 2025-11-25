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

import cvxpy as cp
import numpy as np

x = cp.Variable(3)

objective = cp.Minimize(0.5 * cp.sum_squares(x) + 62 * x[0] + 58 * x[1] + 54 * x[2] - 1280)

constraints = [
    x[0] >= 40,
    x[0] + x[1] >= 100,
    x[0] + x[1] + x[2] >= 180,
    x[0] <= 100,
    x[1] <= 100,
    x[2] <= 100
]

problem = cp.Problem(objective,  constraints)
result = problem.solve()

print("最优解：" , x.value)
print("目标函数值：" , result)
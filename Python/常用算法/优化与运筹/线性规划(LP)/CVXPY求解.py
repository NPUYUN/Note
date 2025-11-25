"""
模型构建
1. 决策变量：x1表示生产甲机床的台数，x2表示生产乙机床的台数。
2. 目标函数：z = 4000x1 + 3000x2，表示最大总利润。
3. 约束条件：
(1) x1 + x2 <= 4，表示每天可用于加工的机器时数为10小时。
(2) 2x1 + x2 <= 8，表示每天可用于加工的机器时数为8小时。
(3) x2 <= 7，表示每天可用于加工的机器时数为7小时。
(4) x1, x2 >= 0，表示生产数量为非负整数。
"""

import cvxpy as cp
from networkx.algorithms.structuralholes import constraint

# 定义决策变量
x = cp.Variable(2)

# 定义目标函数
obj = cp.Maximize(4000 * x[0] + 3000 * x[1])

# 定义约束条件
constraints = [x[0] + x[1] <= 4,
               2 * x[0] + x[1] <= 8,
               x[0] >= 0, x[1] >= 0,
               x[1] <= 7]

# 定义凸优化问题
prob = cp.Problem(obj, constraints)

# 求解凸优化问题
result = prob.solve()

print(x.value)
print(obj.value)


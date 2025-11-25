"""
模型构建
1. 决策变量：$x_1$表示生产甲机床的台数，$x_2$表示生产乙机床的台数。
2. 目标函数：$z = 4000x_1 + 3000x_2$，表示最大总利润。
3. 约束条件：
(1) x1 + x2 <= 4，表示每天可用于加工的机器时数为10小时。
(2) 2x1 + x2 <= 8，表示每天可用于加工的机器时数为8小时。
(3) x2 <= 7，表示每天可用于加工的机器时数为7小时。
(4) x1, x2 >= 0，表示生产数量为非负整数。
"""

import pulp as lp

# 定义线性规划模型
model = lp.LpProblem("The_problem", lp.LpMaximize)

# 定义决策变量
x1 = lp.LpVariable("x1", lowBound=0)
x2 = lp.LpVariable("x2", lowBound=0 , upBound=7)

# 定义目标函数
model += 4000 * x1 + 3000 * x2

# 定义约束条件
model += x1 + x2 <= 4
model += 2 * x1 + x2 <= 8

# 求解线性规划模型
status = model.solve()

print(lp.LpStatus[status])
print(lp.value(x1))
print(lp.value(x2))
print(lp.value(model.objective))


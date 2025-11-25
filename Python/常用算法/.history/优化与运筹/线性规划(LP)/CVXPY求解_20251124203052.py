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


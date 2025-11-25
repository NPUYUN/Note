import pulp as lp

# 定义线性规划模型
model = lp.LpProblem("The_problem", lp.LpMaximize)

# 定义决策变量
x1 = lp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = lp.LpVariable("x2", lowBound=0 , upBound=7, cat="Integer")

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


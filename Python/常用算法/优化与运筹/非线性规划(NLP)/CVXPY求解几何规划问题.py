"""
模型构建：
1. 约束变量：长l，宽w，高h
2. 目标函数：S = 2lw + 2lh + 2hw
3. 约束条件：
(1) lwh = V
(2) l > 0 w > 0 h > 0

"""

import cvxpy as cp

l = cp.Variable(pos=True , name='l')
w = cp.Variable(pos=True , name='w')
h = cp.Variable(pos=True , name='h')
V = int(input("请输入体积："))

objective = cp.Minimize(2 * l * w + 2 * l * h + 2 * h * w)

constraints = [l * w * h == V]

problem = cp.Problem(objective , constraints)

result = problem.solve(gp=True)

print("问题状态", problem.status)
print("最小体积的立方体长宽高为：" , l.value , w.value , h.value)
print("最小表面积为：" , result)

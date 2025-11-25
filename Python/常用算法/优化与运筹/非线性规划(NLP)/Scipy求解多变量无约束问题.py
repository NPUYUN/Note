"""
模型构建
1. 决策变量： s为19英寸售出的数量，t为21英寸售出的数量
2. 目标函数：利润 = 销售收入 - 成本
(1) 19英寸售价p = 339 - 0.01s - 0.003t
(2) 21英寸售价q = 339 - 0.01t - 0.004s
(3) 生产成本：固定成本+变动成本 = 400000 + 195s + 225t
总利润函数P(s ,t) = (339 - 0.01s - 0.003t)s + (339 - 0.01t - 0.004s)t - (400000 + 195s + 225t)
"""

from scipy.optimize import minimize
import numpy as np

def objective_function(x):
    s = x[0]
    t = x[1]
    revenue = (339 - 0.01 * s - 0.003 * t) * s + (339 - 0.01 * t - 0.004 * s) * t
    cost = 400000 + 195 * s + 225 * t
    return -(revenue - cost) # 最小化目标函数，因此返回负值

x0 = np.array([1000 , 1000])

result = minimize(objective_function , x0 , method = 'L-BFGS-B' , bounds = [(0 , None) , (0 , None)])

print("最优解：", result.x)
print("目标函数值：", -result.fun)
print("迭代次数：", result.nit)
print("是否收敛：", result.success)
from scipy.optimize import linprog

# 定义目标函数系数
C = [-4000 , -3000]

# 定义约束条件系数矩阵
A = [[1 , 1],[2 , 1]]

# 定义约束条件右侧向量
B = [4 , 8]

# 定义决策变量的取值范围
x1_bounds = (0 , None)
x2_bounds = (0 , 7)

# 调用linprog函数求解线性规划模型
res = linprog(C , A_ub = A , b_ub = B , bounds = [x1_bounds , x2_bounds])

print(res)
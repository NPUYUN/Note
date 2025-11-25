from scipy.optimize import minimize_scalar
import numpy as np

def object_function(x):
    return x**2 - 8 * np.sin(2 * x + np.pi)

result = minimize_scalar(object_function, bounds=(-10, 10))

print("最优解：" , result.x)
print("最小值：" , result.fun)
print("迭代次数：" , result.nit)
print("函数调用次数：" , result.nfev)
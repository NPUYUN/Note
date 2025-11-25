import cmath
import math

import sympy as sym

x = sym.symbols("x" , real=True)
y = sym.symbols("y" , real=True)

# 1. 复数及其基本运算
## 复数的定义：
z1 = x + sym.I * y  # 定义一般形式的复数 z1 = x + iy
z2 = 1 + 2j # 定义具体数值的复数 z2 = 1 + 2i
z3 = complex(1 , 2) # 使用 complex() 函数定义复数 z3 = 1 + 2i
z4 = complex("1+2j") # 使用字符串定义复数 z4 = 1 + 2i

## 复数的代数运算
### 四则运算
sum_z = z1 + z2  # 加法
diff_z = z1 - z2  # 减法
prod_z = z1 * z2  # 乘法
quot_z = z1 / z2  # 除法


print("相加为", sum_z)
print("相减为", diff_z)
print("相乘为", prod_z)
print("相除为", quot_z)


### 求实部与虚部
real_z1 = sym.re(z1)
imag_z1 = sym.im(z1)
real_z2 = sym.re(z2)
imag_z2 = sym.im(z2)

print("z1的实部为", real_z1)
print("z1的虚部为", imag_z1)
print("z2的实部为", real_z2)
print("z2的虚部为", imag_z2)


### 共轭复数
conj_z1 = sym.conjugate(z1)
conj_z2 = sym.conjugate(z2)

print("z1的共轭复数为", conj_z1)
print("z2的共轭复数为", conj_z2)


# 2. 复数的表示法
## 复平面法：x轴为实轴，y轴为虚轴
### 复数的模
z1 = x + sym.I * y
mod_z1 = sym.Abs(z1) # 计算一般复数的模
print("z1的模为", mod_z1)


### 复数的幅角
z2 = 1 + 1j
arg_z2 = sym.arg(z2) # 使用sympy计算幅角(弧度)
angle = cmath.phase(z2) # 使用cmath计算幅角(弧度)
r0 , rheta0 = cmath.polar(z2) # 极坐标表示法，返回模和幅角
print("z2的幅角为", angle / math.pi)
print("z2的幅角为", arg_z2 / sym.pi)
print("z2的模为", r0)
print("z2的幅角为", rheta0 / math.pi)
###### 注意：sympy和cmath计算的幅角结果一致，均为弧度制，但类型不同，sympy为符号类型，cmath为浮点数类型
###### 使用sympy时应该使用sympy中的常量和函数，如sym.pi，而不是math.pi

deg_z2 = sym.deg(arg_z2) # 使用sympy将弧度转换为角度
degree = math.degrees(angle) # 使用math将弧度转换为角度
print("z2的幅角为", degree)
print("z2的幅角为", deg_z2)


### 复数的三角表示与指数表示
rheta = sym.arg(z1)
r = sym.Abs(z1)
triangular = r * (sym.cos(rheta) + sym.I * sym.sin(rheta)) # 三角表示
exponential = r * sym.exp(sym.I * rheta) # 指数表示
print("z1的三角表示为", triangular)
print("z1的指数表示为", exponential)


# 3. 复数的乘除与幂根运算
## 复数乘积与商
r1 = sym.symbols("r1", positive=True)
r2 = sym.symbols("r2", positive=True)
theta1 = sym.symbols("theta1", real=True)
theta2 = sym.symbols("theta2", real=True)
z1 = r1 * (sym.cos(theta1) + sym.I * sym.sin(theta1))
z2 = r2 * (sym.cos(theta2) + sym.I * sym.sin(theta2))

### 乘积
prod_z = z1 * z2
print("z1与z2的乘积为：" , sym.simplify(prod_z))
print("z1与z2的乘积的模为：" , sym.simplify(sym.Abs(prod_z)))
print("z1与z2的乘积的幅角为：" , sym.simplify(sym.arg(prod_z)))

### 商
quote_z = z1 * z2
print("z1与z2的商为：" , sym.simplify(quote_z))
print("z1与z2的商的模为：" , sym.simplify(sym.Abs(quote_z)))
print("z1与z2的商的幅角为：" , sym.simplify(sym.arg(quote_z)))  
###### 注意：sym.simplify() 函数用于化简表达式，使结果更简洁易读；对于三角形式的复数一般会转换为指数形式

## 幂与根
r = sym.symbols("r", positive=True)
theta = sym.symbols("theta", real=True)
n = sym.symbols("n", integer=True, positive=True)
z = r * (sym.cos(theta) + sym.I * sym.sin(theta))

### 复数的幂
z_pow = z ** n
print("z的n次幂为：" , sym.simplify(z_pow))
print("z的n次幂的模为：" , sym.simplify(sym.Abs(z_pow)))
print("z的n次幂的幅角为：" , sym.simplify(sym.arg(z_pow)))

### 复数的根
w = sym.symbols("w", complex=True)

eq = sym.Eq(w ** n, z)
roots = sym.solve(eq, w) # 求解方程，得到w的值

print("z的n次根为：")
for root in roots:
    print(sym.simplify(root))
###### 注意：求根时，需要具体给出系数n，否则结果会以符号形式表示

# 4. 复变函数
## 复变函数的定义
z = sym.symbols("z", complex=True)
u = sym.Function("u")(sym.re(z), sym.im(z)) # 定义函数u(x , y)
v = sym.Function("f")(sym.re(z), sym.im(z)) # 定义函数v(x , y)

f = u + sym.I * v # 定义复变函数f(z) = u(x , y) + i * v(x , y)

## 映射
### 目前无法得到确切映射后图形的函数，故略

# 5. 复变函数的极限与连续性
x = sym.symbols("x")
y = sym.symbols("y")
z = sym.symbols("z", complex=True)
k = sym.symbols("k")

## 复变函数的极限
f1 = sym.sin(z) / z
print("f1的极限为：" , sym.limit(f1, z, 0)) # 求关于z的函数的极限
print("f1的极限为：" , sym.limit(f1, z, 0 , '+')) # 求关于z的函数的极限0+
print("f1的极限为：" , sym.limit(f1, z, 0 , '-')) # 求关于z的函数的极限0-

f2 = sym.sqrt(x**2 + y**2) / (x + y) # 对于z趋向于0，可以转换为二元函数来求解
paths = [ # 沿着不同路径求极限
    {y: 0},  # 水平路径
    {y: k*x} # 斜线路径
]

results = []
for path in paths:
    exper = f2.subs(path)
    try:
        result = sym.limit(exper, x, 0)
        results.append(result)
    except:
        print("无法求解")

has_result = True
for result in results:
    if result != results[0]:
        has_result = False
        break
if has_result:
    print("f2的极限为：" , results[1])
else:
    print("极限不存在")


## 复变函数的连续性
### 直接生成连续区间
f3 = sym.sin(z) / z
print("f3在复数区间[-1, 1]内的连续区间为：" , sym.calculus.util.continuous_domain(f3, z, sym.Interval(-1, 1)))

### 直接生成间断点
f4 = sym.sin(z) / z
print("f4在复数区间[-1, 1]内的奇点为：" , sym.calculus.singularities(f4, z, sym.Interval(-1, 1)))

### 求函数在该点处的极限与函数在该点处的值是否相等，略



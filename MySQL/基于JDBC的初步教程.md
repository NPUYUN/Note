# 基于JDBC的初步MySQL教程

## 创建数据库
``` sql
create database 数据库名
```


## 创建表
```sql
create table 表名(
    列名1 数据类型 [约束条件] ,
    列名2 数据类型 [约束条件] ,
    ...
    [表级约束条件]
) [engine=存储引擎][charset=字符集];
[]内表示可选项
```
- 存储引擎
  - innodb：支持事务、外键
  - myisan：查询速度快，不支持事务
- 数据类型：
  - 整数：**tinyint**(1字节)，**int**(4字节)，**bigint**(8字节)
  - 浮点：**float**(单精度)，**double**(双精度)，**decimal(精度，小数位)**(任意精度)
  - 字符串：**char(n)**(固定长度)，**varchar(n)**(可变长度)，**text**(长文本)
  - 日期时间：**date**(日期)，**datetime**(日期+时间)，**timestamp**(时间戳)
  - 枚举/集合：**enum('值1','值2')**(单选)，**set('值1','值2')**(多选)
- 约束条件：
  - **NOT NULL**：列值不可为空
  - **PRIMARY KEY**：主键（唯一且非空）
  - **AUTO_INCREMENT**：自增（常用于主键），配合主键使用
  - **DEFAULT 值**：默认值
  - **UNIQUE**：唯一约束
  - 表级约束条件：约束条件(要约束的列名)


## 插入数据
- 基础语法(指定列名)
``` sql
INSERT INTO 表名 (列1, 列2, 列3, ...) VALUES (值1, 值2, 值3, ...);
```

- 简化语法（省略列名，需按表结构顺序填充所有字段）
``` sql
INSERT INTO 表名 VALUES (值1, 值2, 值3, ...);
```


## 查询数据
``` sql
SELECT [DISTINCT] 列名1, 列名2, ... FROM 表名 [WHERE 条件] [ORDER BY 列名 [ASC|DESC]] [LIMIT 偏移量, 行数];
[]内为可选项
```
- DISTINCT：去除重复记录（默认保留所有）
- WHERE：过滤条件（支持比较运算符和逻辑运算符）
- ORDER BY：排序（ASC升序，DESC降序）
- LIMIT：限制返回行数（分页时常用）

列名1，列名2...可替换为：
- *：查询所有数据
- COUNT(*)：查询数据个数
- AVG(列名)：计算平均数
- SUM(列名)：求和
- MAX(列名)：最大值
- MIN(列名)：最小值


## 修改数据
``` sql
UPDATE 表名 SET 列1=新值1, 列2=新值2, ... [WHERE 条件] [ORDER BY 排序列 [ASC|DESC]] [LIMIT 行数];
[]里为可选项
```
- WHERE子句：指定更新范围（**必加**，否则全表更新）
- ORDER BY + LIMIT?：控制更新顺序和数量（避免锁表风险）

## 删除数据
``` sql
DELETE FROM 表名 [WHERE 条件] [ORDER BY 排序列 [ASC|DESC]] [LIMIT 行数];
```


## 备份
在控制台上输入：
``` bash
mysqldump -u [用户名] -p[密码] [数据库名] > [备份文件路径].sql
```
还可以在可视化界面手动备份


## 还原
在控制台中输入：
``` bash
mysql -u [用户名] -p[密码] [目标数据库名] < [备份文件路径].sql
```
还可以在可视化界面手动还原
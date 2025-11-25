# 常用算法大纲
## 分类总览
- 优化与运筹：线性规划（LP）、整数规划（IP/MIP）、非线性规划（NLP）、凸优化、动态规划、网络流、最短路、多目标优化（Pareto、NSGA-II）
- 统计与回归：最小二乘（OLS）、逻辑回归、岭回归/套索（Ridge/Lasso）、广义线性模型（GLM）、分位数回归、稳健回归
- 时间序列：ARIMA/SARIMA、指数平滑（ETS）、状态空间模型（Kalman）、GARCH/EGARCH、Prophet
- 机器学习：决策树/随机森林、梯度提升（XGBoost/LightGBM/CatBoost）、SVM、KNN、神经网络（MLP、RNN/LSTM）、集成学习
- 聚类与降维：K-means、层次聚类、DBSCAN、谱聚类；PCA、SVD、LDA、t-SNE、UMAP
- 仿真与随机：蒙特卡洛（MC）、拉丁超立方采样（LHS）、马尔可夫链、队列论、离散事件仿真、Agent-Based Simulation
- 数值计算：常微分方程（Euler、RK4）、边值问题、偏微分方程（有限差分/有限元/FVM）、数值积分与求根（Newton-Raphson、BFGS）
- 启发式与元启发式：遗传算法（GA）、粒子群（PSO）、模拟退火（SA）、蚁群（ACO）、禁忌搜索（TS）
- 贝叶斯方法：MCMC（Metropolis-Hastings、Gibbs）、变分推断、贝叶斯层次模型
- 网络与图模型：最大流/最小割、匹配、社区发现、中心性、图最优化

## 常见场景 → 算法映射
- 配送/排程/选址：MIP/LP、网络流、禁忌搜索/遗传算法（大规模近似）、多目标优化
- 需求预测与销量：ARIMA/ETS、随机森林/XGBoost、Prophet；特征工程+交叉验证
- 定价与收益管理：NLP/凸优化、动态规划、仿真+贝叶斯更新
- 风险评估与评分：逻辑回归、树模型/提升模型、稳健回归、概率校准（Platt/Isotonic）
- 客群与分层：K-means/层次聚类/DBSCAN，后续用PCA/UMAP可视化；轮廓系数/CH指数评估
- 交通网络与路径：最短路（Dijkstra/A*）、最大流、匹配；不确定性用蒙特卡洛+鲁棒优化
- 能源/工程仿真：ODE/PDE数值、有限元（FEM）、多物理耦合；参数估计用最小二乘/贝叶斯
- 文本与舆情：主题模型（LDA）、词向量/Transformer特征，分类用SVM/提升模型/神经网络
- 金融时序：GARCH/EGARCH、状态空间/卡尔曼、LSTM；换手成本与约束引入优化框架

## 建模流程建议
- 问题定义与指标：明确目标函数、约束、评估指标（MAE、RMSE、F1、成本/收益）
- 数据处理：缺失/异常、标准化、分箱、时间泄露防护、训练/验证/测试划分
- 模型选择与比较：基线模型→复杂模型，交叉验证与网格/贝叶斯搜索调参
- 约束与可解释：在优化中显式建模约束；在预测中加入可解释性（SHAP/特征重要性）
- 不确定性处理：情景分析、鲁棒优化、仿真；区间预测与置信带
- 部署与复盘：性能监控、漂移检测、再训练策略；文档化假设与边界

## Python工具库
- 优化：`PuLP`、`Pyomo`、`cvxpy`、`ortools`、`networkx`（图算法）
- 统计与时序：`statsmodels`、`pmdarima`、`prophet`
- 机器学习：`scikit-learn`、`xgboost`、`lightgbm`、`catboost`
- 仿真与随机：`numpy`/`scipy`（采样/积分）、`simpy`（离散事件）、`SALib`（敏感性分析）
- 数值与PDE：`scipy.integrate`、`pyDOE`/`scikit-optimize`、`FEniCS`/`SfePy`
- 贝叶斯：`pymc`、`stan`/`cmdstanpy`
- 元启发式：`deap`（GA）、`pyswarms`（PSO）

## 快速选型小抄
- 有明确目标+约束 → 优化（LP/MIP/NLP/凸）
- 只需预测/分类 → 回归/树模型/Boosting/神经网络
- 难以解析、需试验 → 仿真+元启发式+鲁棒分析
- 高维可视化/压缩 → PCA/UMAP/t-SNE
- 时间相关性强 → ARIMA/ETS/状态空间/LSTM
- 不确定性与因果 → 贝叶斯/MCMC/实验设计/因果推断
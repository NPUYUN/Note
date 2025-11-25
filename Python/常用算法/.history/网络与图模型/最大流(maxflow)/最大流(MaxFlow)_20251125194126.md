# 最大流
## 基础概念
见**优化与运筹**的**网络流**

## 最大流问题
最大流问题是指在一个网络中，从源点到汇点的最大流量问题。
NetworkX 是一个功能强大的 Python 库，用于创建、操作和研究复杂网络结构。它提供了丰富的功能。
其中求解最大流的核心函数有：
- `maximun_flow (flowG, _s, _t, capacity='capacity', flow_func=None, *kwargs)` 求解最大流问题
- `maximun_flow_value (flowG, _s, _t, capacity='capacity', flow_func=None, *kwargs)` 最大流问题的流量值
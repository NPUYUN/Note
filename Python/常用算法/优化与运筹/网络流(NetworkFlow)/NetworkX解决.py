import networkx as nx

n = int(input("请输入网络节点数："))
m = int(input("请输入网络边数："))
S = int(input("请输入源点编号："))
T = int(input("请输入汇点编号："))

G = nx.DiGraph()
for i in range(m):
    u, v, c, w = map(int, input().split())
    G.add_edge(u, v, weight=w, capacity=c)

flow_dict = nx.max_flow_min_cost(G, S, T)

min_cost = nx.cost_of_flow(G, flow_dict)

max_flow_value = sum(flow_dict[S].values())

print("最小费用：", min_cost)
print("最大流：", max_flow_value)
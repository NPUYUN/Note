import networkx as nx

def shortest_path(G, s, t):
    try:
        print(nx.shortest_path(G, s, t, weight='weight'))
        return nx.shortest_path_length(G, s, t, weight='weight')
    except:
        return -1

G = nx.Graph()

n = int(input("请输入节点数："))
m = int(input("请输入边数："))

for i in range(m):
    u, v, w = map(int, input("请输入边：").split())
    G.add_edge(u, v, weight=w)

print(shortest_path(G, 1, n))
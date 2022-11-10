import networkx as nx
import re
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import netwulf as nw

n, m, r = list(map(int, input().split(" ")))
s, t = input().split(" ")

nodes = []
is_red = []
is_red_dict = {}
for _ in range(n):
    inp = input()
    foo = inp.replace(" *", "").strip()
    nodes.append(foo)
    is_red.append("red" if inp[-1] == "*" else "black")
    is_red_dict[foo] = "red" if inp[-1] == "*" else "black"

inp = None
is_directed = False
edges = []
for _ in range(m):
    inp = input().strip()
    edges.append(re.split(r" -[\->] ", inp))

    if "->" in inp:
        is_directed = True


G = nx.Graph() if not is_directed else nx.DiGraph()
G.add_nodes_from(nodes)
nx.set_node_attributes(G, is_red_dict, name="color")
G.add_edges_from(edges)


def none(G: nx.Graph, s: str, t: str):
    blacks = []
    for key, val in nx.get_node_attributes(G, "color").items():
        if val == "black":
            blacks.append(key)
    _G: nx.Graph = G.subgraph(blacks)
    try:
        return len(nx.shortest_path(_G, source=s, target=t))
    except (ValueError, nx.exception.NodeNotFound, nx.exception.NetworkXNoPath):
        return -1, len(_G.edges)


def few(G, s, t):
    _G = G.copy()
    attr = nx.get_node_attributes(_G, "color")
    for edge in _G.edges:
        _G[edge[0]][edge[1]]["weight"] = (
            1 if attr[edge[1]] == "red" or attr[edge[0]] == "red" else 0
        )
    try:
        path = nx.dijkstra_path(_G, source=s, target=t, weight="weight")
        if len(path) < 20:
            print(path)
            # print(attr)
        path_sum = 0
        for i in range(len(path) - 1):
            path_sum += _G[path[i]][path[i+1]]['weight']
        return path_sum
    except (ValueError, nx.exception.NodeNotFound, nx.exception.NetworkXNoPath):
        return -1

    # nx.shortes_path(_G, source=s, target=t)


print(few(G, s, t))

# nw.visualize(G)
# pos = graphviz_layout(G, prog="dot")
# pos = nx.circular_layout(G)
# labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# nx.draw(G, pos=pos, node_size=10, with_labels=True, node_color=is_red)
# plt.show()


"""Few - dijsktra 
- Shortest path
- Does not work with negative weight
- Give red high weight (1/0)

None
Some 
Many
Few
Alternate 
"""

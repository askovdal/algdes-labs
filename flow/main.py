def edgelist_to_adjmatrix(edgelist, n_nodes):
    adj_matrix = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]
    for edge in edgelist:
        adj_matrix[edge[0]][edge[1]] = float("Inf") if edge[2] == -1 else edge[2]
        adj_matrix[edge[1]][edge[0]] = float("Inf") if edge[2] == -1 else edge[2]
    return adj_matrix


n_nodes = int(input())
nodes = [input() for _ in range(n_nodes)]
n_edges = int(input())
edges = [list(map(int, input().split())) for _ in range(n_edges)]
adj_matrix = edgelist_to_adjmatrix(edges, n_nodes)

from collections import defaultdict
from collections import defaultdict

'''
# This class represents a directed graph
# using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])

    """Returns true if there is a path from
    source 's' to sink 't' in
    residual graph. Also fills
    parent[] to store the path """

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of
            # the dequeued vertex u
            # If a adjacent has not been
            # visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting
        # from source, then return
        # true, else false
        return True if visited[t] else False

    # Function for Depth first search
    # Traversal of the graph
    def dfs(self, graph, s, visited):
        visited[s] = True
        for i in range(len(graph)):
            if graph[s][i] > 0 and not visited[i]:
                self.dfs(graph, i, visited)

    # Returns the min-cut of the given graph
    def minCut(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        visited = len(self.graph) * [False]
        self.dfs(self.graph, s, visited)

        summ = 0

        # print the edges which initially had weights
        # but now have 0 weight
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0 and visited[i]:
                    summ += self.org_graph[i][j]
                    print(str(i) + " - " + str(j) + " - " + str(self.org_graph[i][j]))

        print(summ)



class Graph:
    def __init__(self, graph):
        self.graph = graph

    def BFS(self, s, t, path):
        marked = [False]*(len(self.graph))
        queue = []
        marked[s] = True
        queue.append(s)
        while queue:
            v = queue.pop(0)
            for i, cap in enumerate(self.graph[v]):
                if not marked[i] and cap > 0:
                    marked[i] = True
                    queue.append(i)
                    path[i] = v
                    if i == t:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        path = [-1]*len(self.graph)
        max_flow = 0

        while self.BFS(source, sink, path):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[path[s]][s])
                s = path[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = path[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = path[v]

        return max_flow# , self.graph
'''

from pprint import pprint
# pprint(adj_matrix)
#g = Graph(adj_matrix)
source = 0
sink = n_nodes - 1

#g.minCut(source, sink)


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
print(np.array(adj_matrix))
G = nx.from_numpy_matrix(np.array(adj_matrix), create_using=nx.DiGraph)#, create_using=nx.DiGraph())
print(nx.minimum_cut(G, source, sink, capacity='weight'))
fig, ax = plt.subplots()

pos = nx.circular_layout(G)
nx.draw(G, ax=ax, pos=pos)
plt.show()

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


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def dfs(self, graph, s, visited):
        visited[s] = True
        for i in range(self.ROW):
            if graph[s][i] > 0 and not visited[i]:
                self.dfs(graph, i, visited)

    def min_cut(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        visited = [False] * self.ROW
        self.dfs(self.graph, source, visited)
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i] and not visited[j] and self.org_graph[i][j]:
                    print(f'{i} {j} {self.org_graph[i][j]}')

        return max_flow


g = Graph(adj_matrix)
source = 0
sink = n_nodes - 1

print(g.min_cut(source, sink))

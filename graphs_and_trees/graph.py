from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self):
        V = len(self.graph)
        visited = [False]*V
        for i in range(V):
            if visited[i] == False:
                self.dfs_util(i, visited)
    
    def bfs(self, s):
        visited = [False]*len(self.graph)
        queue = []
        visited[s] = True
        queue.append(s)
        while queue:
            elem = queue.pop()
            print(elem)
            for i in self.graph[elem]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1) 
    graph.add_edge(0, 2) 
    graph.add_edge(1, 2) 
    graph.add_edge(2, 0) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 3)
    print(graph.graph) 
    graph.dfs()
    print("---")
    graph.bfs(2)

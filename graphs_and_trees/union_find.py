from graphs_and_trees.graph import Graph

class UnionFind(Graph):
    def show(self):
        print("Hello")

    def find_parent(self, i, parent):
        # print(i)
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent[i], parent)

    def union(self, parent, x, y):
        # find parent of x and find parent of y
        # set parent y as parent of x
        x_set = self.find_parent(x, parent)
        y_set =self.find_parent(y, parent)
        parent[x_set] = y_set

    def is_cycle(self):
        parent = [-1]*len(self.graph)
        # print(parent)
        for i in self.graph:
            for j in self.graph[i]:
                # find parent for both the nodes of an edge
                x = self.find_parent(i, parent)
                y = self.find_parent(j, parent)
                if x == y:
                    return True
                # If not cycle then do the union of both the nodes
                self.union(parent, x, y)


if __name__ == '__main__':
    g = UnionFind()
    g.add_edge(0,1)
    g.add_edge(1,2)
    # g.add_edge(2,0)
    cycle = g.is_cycle()
    print(cycle)
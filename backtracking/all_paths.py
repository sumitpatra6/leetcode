visited = []
# def dfs(root, graph):
#     print(root)
#     visited.append(root)
#     for children in graph[root]:
#         # if children not in visited:
#         dfs(children, graph)

def find_path(graph):
    # start = 0
    end = len(graph) - 1
    final_result = []
    def dfs(root, result):
        if root == end:
            final_result.append(result[:])
        for children in graph[root]:
            result.append(children)
            dfs(children, result)
            result.pop(-1)
    dfs(0, [0])
    return final_result

# graph =  [[1,2],[3],[3],[]]
# find_path(graph)
graph = [[1,2,3],[2],[3],[]]
print(find_path(graph))

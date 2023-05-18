def topological_sort(graph):
    in_degree = {u : 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = [u for u in graph if in_degree[u] == ]
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        
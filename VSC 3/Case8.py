from heapq import heappop, heappush
def shortes_path(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0 
    heap = [(0,start)]
    while heap:
        (distance, current) = heappop(heap)
        if current == end:
            break
        for neighbor, cost in graph[current].items():
            new_distance = distance + cost 
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(heap, (new_distance, neighbor))
    return distances[end]

graph = {
    "A":{"B": 1, "C":4},
    "B":{"C": 2, "D":5},
    "C":{"D": 1},
    "D":{},
}

start = "B"
end = "C"
print(shortes_path(graph, start, end))
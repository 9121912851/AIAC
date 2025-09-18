import heapq

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Fixed graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []  # It's good practice to include all nodes, even if they have no outgoing edges
}

shortest_paths = dijkstra(graph, 'A')
print("Shortest distances from A:", shortest_paths)

import heapq

def ucs(graph, start, goal):
    # (cost, current_node, path)
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        
        visited.add(node)
        path = path + [node]

        # Goal check
        if node == goal:
            return cost, path

        # Explore neighbors
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [],
    'F': [('G', 2)],
    'G': []
}

result = ucs(graph, 'A', 'G')
print(result)

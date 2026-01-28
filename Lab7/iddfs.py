from collections import deque

# -----------------------------
# Maze (1 = path, 0 = wall)
# -----------------------------
maze = [
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1]
]

start = (0, 0)
goal  = (3, 3)

# -----------------------------
# Common Helper Function
# -----------------------------
def is_valid(maze, x, y, visited):
    rows = len(maze)
    cols = len(maze[0])
    return (
        0 <= x < rows and
        0 <= y < cols and
        maze[x][y] == 1 and
        (x, y) not in visited
    )

# -----------------------------
# BFS (Shortest Path)
# -----------------------------
def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored = 0

    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1

        if (x, y) == goal:
            return path, nodes_explored

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy
            if is_valid(maze, nx, ny, visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored

# -----------------------------
# DFS (Not guaranteed shortest)
# -----------------------------
def dfs_util(maze, current, goal, visited, path, counter):
    counter[0] += 1

    if current == goal:
        return path

    x, y = current
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = x + dx, y + dy
        if is_valid(maze, nx, ny, visited):
            visited.add((nx, ny))
            result = dfs_util(
                maze, (nx, ny), goal, visited, path + [(nx, ny)], counter
            )
            if result:
                return result

    return None

def dfs(maze, start, goal):
    visited = set([start])
    counter = [0]
    path = dfs_util(maze, start, goal, visited, [start], counter)
    return path, counter[0]

# -----------------------------
# IDDFS (Main Objective)
# -----------------------------
def dls(maze, current, goal, limit, visited, path, counter):
    counter[0] += 1

    if current == goal:
        return path
    if limit == 0:
        return None

    x, y = current
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = x + dx, y + dy
        if is_valid(maze, nx, ny, visited):
            visited.add((nx, ny))
            result = dls(
                maze, (nx, ny), goal, limit - 1,
                visited, path + [(nx, ny)], counter
            )
            if result:
                return result
            visited.remove((nx, ny))

    return None

def iddfs(maze, start, goal, max_depth=50):
    total_nodes = 0

    for depth in range(max_depth):
        visited = set([start])
        counter = [0]
        result = dls(maze, start, goal, depth, visited, [start], counter)
        total_nodes += counter[0]

        if result:
            return result, total_nodes

    return None, total_nodes

# -----------------------------
# Run All Algorithms
# -----------------------------
bfs_path, bfs_nodes = bfs(maze, start, goal)
dfs_path, dfs_nodes = dfs(maze, start, goal)
iddfs_path, iddfs_nodes = iddfs(maze, start, goal)

print("BFS Path:", bfs_path)
print("BFS Nodes Explored:", bfs_nodes)

print("\nDFS Path:", dfs_path)
print("DFS Nodes Explored:", dfs_nodes)

print("\nIDDFS Path:", iddfs_path)
print("IDDFS Nodes Explored:", iddfs_nodes)

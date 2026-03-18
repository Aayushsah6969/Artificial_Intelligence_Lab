from collections import deque
import heapq


grid = [
    "#########",
    "#S.B...E#",
    "#.......#",
    "#.......#",
    "#.......#",
    "#A.....C#",
    "#########",
]

# Higher number = more important goal
goal_priority = {
    "A": 10,
    "B": 1,
    "C": 2,
}


def parse_grid(grid):
    start = None
    exit_pos = None
    goals = {}

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cell = grid[r][c]
            if cell == "S":
                start = (r, c)
            elif cell == "E":
                exit_pos = (r, c)
            elif cell in goal_priority:
                goals[cell] = (r, c)

    return start, exit_pos, goals


def get_neighbors(position):
    r, c = position
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if grid[nr][nc] != "#":
            neighbors.append((nr, nc))

    return neighbors


def get_goal_name(position, goals):
    for name, goal_pos in goals.items():
        if goal_pos == position:
            return name
    return None


def reconstruct_path(parent, final_state):
    path = []
    state = final_state

    while state is not None:
        position, _ = state
        path.append(position)
        state = parent[state]

    path.reverse()
    return path


def print_path_on_grid(path):
    temp = [list(row) for row in grid]

    for r, c in path:
        if temp[r][c] == ".":
            temp[r][c] = "*"

    for row in temp:
        print("".join(row))


def goal_order_from_path(path):
    _, _, goals = parse_grid(grid)
    order = []

    for position in path:
        goal_name = get_goal_name(position, goals)
        if goal_name and goal_name not in order:
            order.append(goal_name)

    return order


def bfs_search():
    start, exit_pos, goals = parse_grid(grid)
    all_goals = frozenset(goals.keys())

    start_state = (start, frozenset())
    queue = deque([start_state])
    visited = {start_state}
    parent = {start_state: None}

    while queue:
        position, collected = queue.popleft()

        if position == exit_pos and collected == all_goals:
            return reconstruct_path(parent, (position, collected))

        for next_pos in get_neighbors(position):
            new_collected = collected
            goal_name = get_goal_name(next_pos, goals)

            if goal_name:
                new_collected = frozenset(set(collected) | {goal_name})

            if next_pos == exit_pos and new_collected != all_goals:
                continue

            next_state = (next_pos, new_collected)

            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (position, collected)
                queue.append(next_state)

    return None


def dfs_search():
    start, exit_pos, goals = parse_grid(grid)
    all_goals = frozenset(goals.keys())

    start_state = (start, frozenset())
    stack = [start_state]
    visited = {start_state}
    parent = {start_state: None}

    while stack:
        position, collected = stack.pop()

        if position == exit_pos and collected == all_goals:
            return reconstruct_path(parent, (position, collected))

        for next_pos in reversed(get_neighbors(position)):
            new_collected = collected
            goal_name = get_goal_name(next_pos, goals)

            if goal_name:
                new_collected = frozenset(set(collected) | {goal_name})

            if next_pos == exit_pos and new_collected != all_goals:
                continue

            next_state = (next_pos, new_collected)

            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (position, collected)
                stack.append(next_state)

    return None


def weighted_step_cost(collected):
    remaining_priority = 0

    for goal, priority in goal_priority.items():
        if goal not in collected:
            remaining_priority += priority

    return 1 + remaining_priority


def uniform_cost_search():
    start, exit_pos, goals = parse_grid(grid)
    all_goals = frozenset(goals.keys())

    start_state = (start, frozenset())
    pq = [(0, start_state)]
    parent = {start_state: None}
    best_cost = {start_state: 0}

    while pq:
        current_cost, (position, collected) = heapq.heappop(pq)

        if current_cost > best_cost[(position, collected)]:
            continue

        if position == exit_pos and collected == all_goals:
            path = reconstruct_path(parent, (position, collected))
            return path, current_cost

        for next_pos in get_neighbors(position):
            new_collected = collected
            goal_name = get_goal_name(next_pos, goals)

            if goal_name:
                new_collected = frozenset(set(collected) | {goal_name})

            if next_pos == exit_pos and new_collected != all_goals:
                continue

            next_state = (next_pos, new_collected)
            new_cost = current_cost + weighted_step_cost(new_collected)

            if next_state not in best_cost or new_cost < best_cost[next_state]:
                best_cost[next_state] = new_cost
                parent[next_state] = (position, collected)
                heapq.heappush(pq, (new_cost, next_state))

    return None, None


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def heuristic(position, collected, exit_pos, goals):
    remaining = []

    for name, goal_pos in goals.items():
        if name not in collected:
            remaining.append(goal_pos)

    if not remaining:
        return manhattan(position, exit_pos)

    best = float("inf")
    for goal_pos in remaining:
        value = manhattan(position, goal_pos) + manhattan(goal_pos, exit_pos)
        best = min(best, value)

    return best


def a_star_search():
    start, exit_pos, goals = parse_grid(grid)
    all_goals = frozenset(goals.keys())

    start_state = (start, frozenset())
    pq = [(heuristic(start, frozenset(), exit_pos, goals), 0, start_state)]
    parent = {start_state: None}
    best_cost = {start_state: 0}

    while pq:
        _, current_cost, (position, collected) = heapq.heappop(pq)

        if current_cost > best_cost[(position, collected)]:
            continue

        if position == exit_pos and collected == all_goals:
            path = reconstruct_path(parent, (position, collected))
            return path, current_cost

        for next_pos in get_neighbors(position):
            new_collected = collected
            goal_name = get_goal_name(next_pos, goals)

            if goal_name:
                new_collected = frozenset(set(collected) | {goal_name})

            if next_pos == exit_pos and new_collected != all_goals:
                continue

            next_state = (next_pos, new_collected)
            new_cost = current_cost + weighted_step_cost(new_collected)

            if next_state not in best_cost or new_cost < best_cost[next_state]:
                best_cost[next_state] = new_cost
                parent[next_state] = (position, collected)
                estimate = new_cost + heuristic(next_pos, new_collected, exit_pos, goals)
                heapq.heappush(pq, (estimate, new_cost, next_state))

    return None, None


def show_result(name, path, cost=None):
    print("\n" + "=" * 40)
    print(name)
    print("=" * 40)

    if path is None:
        print("No path found")
        return

    print("Path:", path)
    print("Steps:", len(path) - 1)
    print("Goal Order:", goal_order_from_path(path))
    if cost is not None:
        print("Weighted Cost:", cost)
    print_path_on_grid(path)


bfs_path = bfs_search()
dfs_path = dfs_search()
ucs_path, ucs_cost = uniform_cost_search()
astar_path, astar_cost = a_star_search()

show_result("BFS (Unweighted)", bfs_path)
show_result("DFS (Unweighted)", dfs_path)
show_result("Uniform Cost Search (Weighted)", ucs_path, ucs_cost)
show_result("A* Search (Weighted)", astar_path, astar_cost)

print("\nTrade-off Analysis")
print("Goal Priorities:", goal_priority)
print("- BFS gives the shortest path when all goals are treated equally.")
print("- DFS can find a solution, but the path may be longer than BFS.")
print("- UCS and A* consider goal priority. Delaying a high-priority goal increases total cost.")
print("- Because of that, a weighted search may choose a longer route if it collects important goals earlier.")

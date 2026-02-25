import time
import heapq
from collections import deque
from copy import deepcopy

# ==============================
# Game Utilities
# ==============================

EMPTY = " "
PLAYER_X = "X"  # AI
PLAYER_O = "O"  # Opponent

WIN_PATTERNS = [
    [0,1,2],[3,4,5],[6,7,8],  # rows
    [0,3,6],[1,4,7],[2,5,8],  # cols
    [0,4,8],[2,4,6]           # diagonals
]

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

def check_winner(board):
    for pattern in WIN_PATTERNS:
        values = [board[i] for i in pattern]
        if values[0] != EMPTY and values.count(values[0]) == 3:
            return values[0]
    if EMPTY not in board:
        return "DRAW"
    return None

def get_next_player(board):
    return PLAYER_X if board.count(PLAYER_X) == board.count(PLAYER_O) else PLAYER_O

def get_successors(board):
    successors = []
    player = get_next_player(board)
    for i in range(9):
        if board[i] == EMPTY:
            new_board = board.copy()
            new_board[i] = player
            successors.append(new_board)
    return successors

def board_to_tuple(board):
    return tuple(board)

# ==============================
# Heuristic for A*
# ==============================

def heuristic(board):
    """
    Simple heuristic:
    +10 if X wins
    -10 if O wins
    Otherwise: count potential winning lines for X minus O
    """
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 10
    if winner == PLAYER_O:
        return -10

    score = 0
    for pattern in WIN_PATTERNS:
        line = [board[i] for i in pattern]
        if PLAYER_O not in line:
            score += 1
        if PLAYER_X not in line:
            score -= 1
    return score

# ==============================
# BFS Search
# ==============================

def bfs_search(start_board):
    start_time = time.time()
    queue = deque([(start_board, [])])
    visited = set()
    nodes = 0

    while queue:
        board, path = queue.popleft()
        nodes += 1

        winner = check_winner(board)
        if winner == PLAYER_X:
            return path + [board], nodes, time.time() - start_time

        key = board_to_tuple(board)
        if key in visited:
            continue
        visited.add(key)

        for succ in get_successors(board):
            queue.append((succ, path + [board]))

    return None, nodes, time.time() - start_time

# ==============================
# DFS Search
# ==============================

def dfs_search(start_board):
    start_time = time.time()
    stack = [(start_board, [])]
    visited = set()
    nodes = 0

    while stack:
        board, path = stack.pop()
        nodes += 1

        winner = check_winner(board)
        if winner == PLAYER_X:
            return path + [board], nodes, time.time() - start_time

        key = board_to_tuple(board)
        if key in visited:
            continue
        visited.add(key)

        for succ in get_successors(board):
            stack.append((succ, path + [board]))

    return None, nodes, time.time() - start_time

# ==============================
# A* Search
# ==============================

def astar_search(start_board):
    start_time = time.time()
    pq = []
    heapq.heappush(pq, (0, 0, start_board, []))
    visited = set()
    nodes = 0

    while pq:
        f, g, board, path = heapq.heappop(pq)
        nodes += 1

        winner = check_winner(board)
        if winner == PLAYER_X:
            return path + [board], nodes, time.time() - start_time

        key = board_to_tuple(board)
        if key in visited:
            continue
        visited.add(key)

        for succ in get_successors(board):
            g_new = g + 1
            h_new = -heuristic(succ)  # negative because we want to maximize X
            f_new = g_new + h_new
            heapq.heappush(pq, (f_new, g_new, succ, path + [board]))

    return None, nodes, time.time() - start_time

# ==============================
# Comparison Runner
# ==============================

def compare_algorithms(start_board):
    print("Initial Board:")
    print_board(start_board)

    print("Running BFS...")
    _, bfs_nodes, bfs_time = bfs_search(start_board)

    print("Running DFS...")
    _, dfs_nodes, dfs_time = dfs_search(start_board)

    print("Running A*...")
    _, astar_nodes, astar_time = astar_search(start_board)

    print("\n=== Comparison ===")
    print(f"BFS  -> Nodes: {bfs_nodes}, Time: {bfs_time:.4f}s")
    print(f"DFS  -> Nodes: {dfs_nodes}, Time: {dfs_time:.4f}s")
    print(f"A*   -> Nodes: {astar_nodes}, Time: {astar_time:.4f}s")

# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    # Example partially filled board
    start = [
        "X", "O", "X",
        " ", "O", " ",
        " ", " ", " "
    ]

    compare_algorithms(start)
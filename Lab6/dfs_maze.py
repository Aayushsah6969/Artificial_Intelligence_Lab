# Step 1: Define Maze Configuration
MAZE_SIZE = 6
OBSTACLES = {
    (0, 1), (1, 1), 
    (3, 2), (3, 3), (3, 4), (3, 5), 
    (0, 4), 
    (4, 1), (4, 2), (4, 3)
}
START = (0, 0)
GOAL = (0, 5)

# Step 2: Helper function to check if a move is valid
def is_valid(x, y):
    # Check if coordinates are within bounds (0 to 5)
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        # Check if the position is NOT an obstacle
        if (x, y) not in OBSTACLES:
            return True
    return False

# Step 3: Depth-First Search (DFS) Function
def dfs(current, visited, path):
    x, y = current
    
    # Base Case: If we reached the goal
    if current == GOAL:
        path.append(current)
        return True
    
    # Mark the current node as visited
    visited.add(current)
    
    # Define possible moves: Left, Right, Up, Down
    # Corrected typos from the PDF here
    moves = [
        (x - 1, y), # Left
        (x + 1, y), # Right
        (x, y - 1), # Up
        (x, y + 1)  # Down
    ]
    
    # Try each move
    for move in moves:
        if is_valid(move[0], move[1]) and move not in visited:
            # Recursive call: if this path leads to the goal, return True
            if dfs(move, visited, path):
                path.append(current) # Add current node to path (backtracking)
                return True
                
    return False

# Step 4: Main Execution
visited_nodes = set()
final_path = []

print(f"Solving Maze from {START} to {GOAL}...")

if dfs(START, visited_nodes, final_path):
    # The path is constructed in reverse order during recursion (Goal -> Start)
    final_path.reverse()
    
    print("Success! Path found:")
    print(final_path)
    
    # Visualizing the move count
    print(f"Total steps: {len(final_path)}")
else:
    print("No path found!")
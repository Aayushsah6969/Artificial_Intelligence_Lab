###
# Objective: Implement BFS and DFS to solve a maze.

# Problem Statement: Given a grid-based maze where 0 represents walls and 1 represents walkable paths, find the
# shortest path from a start cell to an end cell.

# Tasks:
# • Use BFS to find the shortest path.
# • Use DFS to explore all possible paths and report one valid path (not necessarily the shortest).
# • Compare the number of nodes explored by BFS and DFS.

###

# We need to import 'deque' (pronounced "deck") - it's like a special list
# that lets us quickly add/remove items from both ends. Think of it like a line of people
# where you can add people at the front OR back, and remove them from front OR back!
from collections import deque

# BFS = Breadth-First Search
# This function explores the maze layer by layer, like ripples in water spreading out
# It finds the SHORTEST path because it checks all close spots first, then farther spots
def bfs(maze, start, end):
    # First, let's figure out how big our maze is
    rows = len(maze)  # How many rows (going down)
    cols = len(maze[0])  # How many columns (going across)

    # Create our queue - this is like a "to-do list" of places we need to check
    # We'll always check the oldest item first (like standing in a line)
    queue = deque()
    queue.append((start, [start]))  # Add our starting position and the path we took to get there

    # Create a "visited" set - this remembers which cells we've already checked
    # We use a 'set' because it's super fast to check "have I been here before?"
    visited = set()
    visited.add(start)  # Mark our starting spot as visited

    # Keep count of how many cells we looked at (for comparison with DFS later)
    nodes_explored = 0

    # Keep exploring while we still have places to check in our queue
    while queue:
        # Take out the first item from our to-do list (the oldest one)
        (r, c), path = queue.popleft()  # r = row, c = column, path = how we got here
        nodes_explored += 1  # Count this as one cell we explored

        # Are we at the treasure (end goal)? If yes, we found it!
        if (r, c) == end:
            return path, nodes_explored  # Return the path we took and how many cells we checked

        # Now let's check all 4 directions we can move: up, down, left, right
        # (-1,0) = up, (1,0) = down, (0,-1) = left, (0,1) = right
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc  # Calculate the new position (nr = new row, nc = new column)

            # Check if this new position is a valid move:
            if (0 <= nr < rows and  # Is it inside the maze (not above or below)?
                0 <= nc < cols and  # Is it inside the maze (not left or right of boundaries)?
                maze[nr][nc] == 1 and  # Is it a walkable path (1) and not a wall (0)?
                (nr, nc) not in visited):  # Have we NOT been here before?

                # This is a good spot! Let's remember we've been here
                visited.add((nr, nc))
                # Add it to our to-do list with the updated path
                queue.append(((nr, nc), path + [(nr, nc)]))

    # If we get here, we checked everything but didn't find the end
    return None, nodes_explored  # Return None (meaning "no path found")


# DFS = Depth-First Search
# This function explores the maze by going as deep as possible in one direction first
# It's like exploring a cave - you go all the way down one tunnel before trying another
# This is a RECURSIVE function - it calls itself! (like a mirror reflecting a mirror)
def dfs(maze, current, end, visited, path, nodes):
    # Count this cell as explored (we use nodes[0] because it's a list - this lets us update it)
    nodes[0] += 1

    # Did we reach the treasure (end)? If yes, we're done!
    if current == end:
        return True  # Return True means "Success! We found the path!"

    # Get our current position
    r, c = current  # r = current row, c = current column
    # Get the maze size
    rows = len(maze)
    cols = len(maze[0])

    # Try moving in all 4 directions: up, down, left, right
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc  # Calculate new position

        # Check if this move is valid (same checks as BFS)
        if (0 <= nr < rows and  # Inside maze vertically?
            0 <= nc < cols and  # Inside maze horizontally?
            maze[nr][nc] == 1 and  # Is it a walkable path?
            (nr, nc) not in visited):  # Haven't been here yet?

            # Mark this cell as visited so we don't go in circles
            visited.add((nr, nc))
            # Add this cell to our path
            path.append((nr, nc))

            # Now here's the recursive magic! We call DFS again from this new position
            # It's like sending a mini-explorer from here to continue the search
            if dfs(maze, (nr, nc), end, visited, path, nodes):
                return True  # If the mini-explorer found the end, we're done!

            # If we get here, this path was a dead-end, so we need to BACKTRACK
            # Backtracking means "oops, wrong way, let's go back and try another direction"
            path.pop()  # Remove the last step from our path

    # If we tried all directions and none worked, return False (this path failed)
    return False



# Our maze! Think of it like a grid:
# 1 = walkable path (you can step here)
# 0 = wall (you can't go through)
maze = [
    [1, 1, 0, 1],  # Row 0: Start here → path → WALL → path
    [0, 1, 0, 1],  # Row 1: WALL → path → WALL → path
    [1, 1, 1, 1],  # Row 2: All paths (easy row!)
    [0, 0, 1, 1]   # Row 3: WALL → WALL → path → End here!
]

# Where do we start? Top-left corner (row 0, column 0)
start = (0, 0)
# Where do we want to go? Bottom-right corner (row 3, column 3)
end = (3, 3)

# Let's try BFS first!
print("\n=== Running BFS (Breadth-First Search) ===")
bfs_path, bfs_nodes = bfs(maze, start, end)  # Run BFS and get the path + nodes explored

# Now let's try DFS!
print("\n=== Running DFS (Depth-First Search) ===")
dfs_path = [start]  # Start with just the starting position in our path
dfs_nodes = [0]  # Use a list so DFS can update the count (lists are mutable)
dfs(maze, start, end, set([start]), dfs_path, dfs_nodes)  # Run DFS

# Show the results!
print("\n" + "="*50)
print("RESULTS:")
print("="*50)
print("BFS Path (Shortest):", bfs_path)
print("BFS Nodes Explored:", bfs_nodes)

print("\nDFS Path (Any valid):", dfs_path)
print("DFS Nodes Explored:", dfs_nodes[0])


# BFS is used to find the shortest path in a maze by exploring level-wise, while DFS explores depth-wise and finds any valid path without guaranteeing optimality.
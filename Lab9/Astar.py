import heapq

GOAL = ((1,2,3),(4,5,6),(7,8,0))

MOVES = [(-1,0),(1,0),(0,-1),(0,1)] # this is the available moves for the blank tile (0)
# up down left right

# heuristic value calculating functions
def misplaced(state):
    return sum(
        1 for i in range(3) for j in range(3)
        if state[i][j] != 0 and state[i][j] != GOAL[i][j]
    )

def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x,y = divmod(val-1,3)
                dist += abs(x-i)+abs(y-j)
    return dist

#  this function generates the neighboring states by moving the blank tile in the four possible directions and returns a list of valid neighboring states.
def get_neighbors(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                x,y=i,j
    neighbors=[]
    for dx,dy in MOVES:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            s=[list(r) for r in state]
            s[x][y],s[nx][ny]=s[nx][ny],s[x][y]
            neighbors.append(tuple(tuple(r) for r in s))
    return neighbors

def astar(start,heuristic):
    openlist=[]
    heapq.heappush(openlist,(0,start))
    g={start:0} #cost form start to the current node
    visited=set() #we will not visit the explored node
    nodes=0

    while openlist:
        f,state=heapq.heappop(openlist)
        nodes+=1
        
        if state==GOAL:
            return g[state],nodes
        
        visited.add(state)

        for n in get_neighbors(state):
            if n in visited:
                continue
            newg=g[state]+1
            if n not in g or newg<g[n]:
                g[n]=newg
                f=newg+heuristic(n)
                heapq.heappush(openlist,(f,n))
    return None

start=((1,2,3),(4,0,6),(7,5,8))

d1,n1=astar(start,misplaced)
d2,n2=astar(start,manhattan)

print("H1 Misplaced -> depth:",d1," nodes:",n1)
print("H2 Manhattan -> depth:",d2," nodes:",n2)

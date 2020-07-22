# BFS, bfs(幅優先探索)
from collections import deque
r, c = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
maze = [input() for _ in range(r)]

q = deque([[sx-1, sy-1]])
maze_n = [[-1] * c for _ in range(r)]
maze_n[sx-1][sy-1] = 0
while (q):
    vx, vy = q.popleft()
    if (maze[vx - 1][vy] == ".") & (maze_n[vx-1][vy]==-1):
        maze_n[vx - 1][vy] = maze_n[vx][vy] + 1
        q.append([vx - 1,vy])
    if (maze[vx + 1][vy] == ".") &((maze_n[vx+1][vy]==-1)):
        maze_n[vx + 1][vy] = maze_n[vx][vy] + 1
        q.append([vx + 1,vy])
    if (maze[vx][vy - 1] == ".") & (maze_n[vx][vy-1]==-1):
        maze_n[vx][vy - 1] = maze_n[vx][vy] + 1
        q.append([vx, vy - 1])
    if (maze[vx][vy + 1] == ".") &(maze_n[vx][vy+1]==-1):
        maze_n[vx][vy + 1] = maze_n[vx][vy] + 1
        q.append([vx, vy + 1])
    #print(q)

#for k in maze_n:
    #print(k)
print(maze_n[gx - 1][gy - 1])





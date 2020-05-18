from collections import deque

H, W = map(int, input().split())
H += 2; W += 2
grid = []
grid.append(["#" * W])
for h in range(H-2):
  grid.append(["#" + input() + "#"])
grid.append(["#" * W])

INF = 10**9
ans = 0
for h in range(1, H-1):
  for w in range(1, W-1):
    m_grid = 0
    if grid[h][0][w]=="#": continue

    dist = [[INF]*W for i in range(H)]
    dist[h][w] = 0 
    q = deque([(h,w)])

    while(q):
      v_h, v_w = q.popleft()
      d_v = dist[v_h][v_w]
      m_grid = max(d_v, m_grid)
      for n_h, n_w in ((v_h, v_w-1),(v_h, v_w+1),(v_h-1, v_w),(v_h+1, v_w)):
        if grid[n_h][0][n_w]=="#": continue
        d_n = d_v + 1
        if d_n > dist[n_h][n_w]: continue

        dist[n_h][n_w] = d_n
        q.append((n_h,n_w))
        m_grid = max(d_n, m_grid)

    
    ans = max(ans, m_grid)

print(ans)

      


    

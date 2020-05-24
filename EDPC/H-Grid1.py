H, W = map(int, input().split())
grid = []
for h in range(H):
  S = input()
  tmp = []
  for s in S:
    tmp.append(s)
  grid.append(tmp)


dp = [[0]*W for _ in range(H)]
dp[H-1][W-1] = 1

for h in reversed(range(H)):
  for w in reversed(range(W)):
    if (h+1) <= (H-1):
      dp[h][w] += dp[h+1][w]
    if (w+1) <= (W-1):
      dp[h][w] += dp[h][w+1]
    if grid[h][w] == "#":
      dp[h][w] = 0
    
      
print(dp[0][0] % (10**9 + 7))
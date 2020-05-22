N, W = map(int, input().split())
w_list = []
v_list = []
for _ in range(N):
  w, v = map(int, input().split())
  w_list.append(w)
  v_list.append(v)

#w_list.insert(0,0)#アイテム番号を1インデックスに変更.
#v_list.insert(0,0)#アイテム番号を1インデックスに変更.

INF = 10**12
dp = [[INF]*(max(v_list)*N+1) for _ in range(N+1)]
dp[0][0] = 0

#print(dp)

for i in range(1,N+1):
  for j in range(max(v_list)*N+1):
    #print(i,j)
    if j - v_list[i-1] >= 0:
      dp[i][j] = min(dp[i-1][j], dp[i-1][j-v_list[i-1]] + w_list[i-1])
    else:
      dp[i][j] = dp[i-1][j]
  #print(dp)


ans = 0
for j in range(max(v_list)*N+1):
  if dp[N][j] <= W:
    ans = max(ans, j)

print(ans)
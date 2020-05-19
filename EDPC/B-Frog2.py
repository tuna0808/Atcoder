N, K = map(int, input().split())
h = list(map(int, input().split()))
h.insert(0, -1)
INF = 100100100100
dp_table = [INF]*(N+1)
dp_table[0] = -1
dp_table[1] = 0

for i in range(2, N+1): # 各足場i(2~N)を緩和.
  for k in range(1,K+1): # 各足場i(2~N)について高々K通りの遷移.
    if i-k <=0: break #足場i-kからの遷移をみるが足場の最小は1. だから, 0以下になったらbreak.
    dp_table[i] = min(dp_table[i], dp_table[i-k] + abs(h[i]-h[i-k]))
print(dp_table[N])
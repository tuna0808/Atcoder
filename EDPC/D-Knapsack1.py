N, W = map(int, input().split())
kpsk_list = [list(map(int, input().split())) for _ in range(N)]
#print(kpsk_list)
dp = [[0]*(W+1) for _ in range(N+1)]
#print(dp)
for n in range(1, N+1): #何個目までのアイテムを考慮するか
  for w in range(W+1): #各重さでの価値の最大値を求める.
    #print(f"n:{n},w:{w}")
    if w - kpsk_list[n-1][0] < 0: 
      dp[n][w] = dp[n-1][w]
    else:
      dp[n][w] = max(dp[n-1][w], dp[n-1][w - kpsk_list[n-1][0]] + kpsk_list[n-1][1])
    #print(dp)

print(dp[N][W])
  # dp[n]について各重さsum_w(=0~W)の時の最大価値をdpテーブルに保存していく.

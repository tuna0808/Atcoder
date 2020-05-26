N = int(input())
p = list(map(float, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]# dp[i][j]: i枚目まで投げた時, j枚表になってる確率.(i枚の選び方によって変わらん?(dp[N][:]だけみるから途中はどんな順番でもいいってこと？))
dp[0][0] = 1 # 0枚投げた時は, 0枚が表っていう事象しかあり得ない.(dp[0][0]=1で,dp[0][1:]=0)

for i in range(1, N+1):
  for j in range(0, N+1):
    if j - 1 < 0:
      dp[i][j] = dp[i-1][j]*(1-p[i-1])
    else:
      dp[i][j] = (dp[i-1][j-1]*p[i-1]) + (dp[i-1][j]*(1-p[i-1]))

if N % 2==0:
  ans = sum(dp[N][int(N/2):])
else:
  ans = sum(dp[N][int(N//2)+1:])

print(ans)





    
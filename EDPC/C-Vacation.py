N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

dp = [[0,0,0] for _ in range(N+1)]
#print(dp)
for i in range(1,N+1):
  #print(f'i:{i}')
  dp[i][0] = max(dp[i-1][1] + abc[i-1][0], dp[i-1][2] + abc[i-1][0])
  dp[i][1] = max(dp[i-1][0] + abc[i-1][1], dp[i-1][2] + abc[i-1][1])
  dp[i][2] = max(dp[i-1][0] + abc[i-1][2], dp[i-1][1] + abc[i-1][2])
  #print(dp)

print(max(dp[N]))
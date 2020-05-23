import sys
sys.setrecursionlimit(200000)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
MEMO = [-1 for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, input().split())
  G[x].append(y)


def dp_LP(v):# 頂点nから始まる最長経路を返す.
  if MEMO[v] != -1:
    return MEMO[v]
  else:
    ans = 0
    for i in G[v]:
      ans = max(ans, dp_LP(i)+1)
    MEMO[v] = ans

    return ans



answer = 0
for n in range(1,N+1):
  answer = max(answer, dp_LP(n))
print(answer)



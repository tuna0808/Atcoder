import math
"""
N, K = map(int, input().split())
ans = 0

for i in range(1,N+1):
    tmp = math.log(K/i, 2)
    x = int(math.log(K/i,2))
    if i >= K:
        ans += 1/N
    else:
        if tmp - x != 0:
            x += 1
        ans += 1/N * (0.5)**x
"""

N, K = map(int, input().split())
coin = [0.5**k for k in range(10**5)]
ans = 0
for i in range(1,N+1):
    x = 0
    while(True):
        if i*(2**x) >= K:
            ans += 1/N * coin[x]
            break
        else: x += 1

print(ans)

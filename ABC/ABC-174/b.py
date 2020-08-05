import math
N, D = map(int, input().split())
X = []
Y = []
ans = 0
for i in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(N):
    if math.sqrt(X[i]** 2 + Y[i]** 2) <= D:
        ans += 1
print(ans)
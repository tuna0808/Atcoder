# しゃくとり法
N = int(input())
a = list(map(int, input().split()))
cnt = 0
r = 0

for l in range(N):
    while (r+1 < N):
        if (a[r] < a[r+1]):
            r += 1
        else: break
    cnt += (r - l) + 1
    if r == l: r += 1
    
print(cnt)

# imos法
n, m = map(int, input().split())
l = []
r = []
imos = [0]*(n+1)
for i in range(m):
    L, R = map(int, input().split())
    l.append(L)
    r.append(R)

for i in range(m):
    imos[l[i]-1] += 1
    imos[r[i]] -= 1

cum_sum = [imos[0]]
for i in range(1, len(imos)):
    cum_sum.append(cum_sum[i - 1] + imos[i])

ans = 0
for count in cum_sum:
    if count == m: ans += 1
print(ans)

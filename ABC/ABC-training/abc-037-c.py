# 累積和
N, K = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
sum_a = [0]

for i in range(1,N+1):
  sum_a.append(sum_a[i-1] + a[i-1])

for i in range(K, N+1):
  ans += sum_a[i] - sum_a[i-K]

print(ans)

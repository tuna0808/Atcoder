N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = 0
#print(t)
for i in range(1, N):
  ans += min(T, t[i]-t[i-1])
  #print(ans)
  #print()

print(ans+T)
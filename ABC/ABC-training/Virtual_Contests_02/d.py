from fractions import gcd

N, M = map(int, input().split())
S = input()
T = input()

dic = {}
L = int((N*M) / gcd(N,M))
ans = L

for i in range(N):
  dic[int(i*(L/N)+1)] = i

key = set(dic.keys())
for i in range(M):
  if i*(L/M)+1 in key:
    if S[dic[int(i*(L/M)+1)]] == T[i]:continue
    else: 
      ans = -1
      break

  


print(ans)

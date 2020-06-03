N, K = map(int, input().split())
P = list(map(int, input().split()))
ans = 0

E = [(1+p)/2 for p in P]
S = [0]
for i in range(len(E)):
    S.append(S[i] + E[i])

for j in range(K, len(S)):
    ans = max(ans, S[j]-S[j-K])
print(ans)

N, K = map(int, input().split())
A = list(map(int, input().split()))
imos = [0]*(N+1)

# 全体でO(NlogN) ≒ 10^6
for k in range(K): # 下のifによってO(logN)で抑えられる.
    if min(A) == N:
        break

    imos = [0]*(N+1)
    for i,a in enumerate(A): # O(N)
        imos[max(0, i-a)] += 1
        imos[min(N, i + a + 1)] -= 1
        
    A = [imos[0]]
    for i in range(1,len(imos)-1): # O(N)
        A.append(A[i - 1] + imos[i])
        
print(*A, sep=" ")
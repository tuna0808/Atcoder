N, M = map(int, input().split())
neib = {}
ans = 0
for i in range(1,N+1):
    neib[i] = [i]

for _ in range(M):
    A, B = map(int, input().split())
    neib[A].append(B)
#print(neib)
for i in neib.keys():
    





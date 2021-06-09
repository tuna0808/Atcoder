N, K = map(int, input().split())
friends = {}
for n in range(N):
    A, B = map(int, input().split())
    if A in friends: friends[A] += B
    else: friends[A] = B

friends = sorted(friends.items(), key=lambda x:x[0])
ans = K

for v,m in friends:
    if v <= K:
        K += m
        #K -= v
    else:
        continue
    #print(K)
print(K)


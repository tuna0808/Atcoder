N, K = map(int, input().split())
ans = 0
for n in range(1,N+1):
    for k in range(1,K+1):
        ans += int(str(n)+"0"+str(k))
    #print(ans)
print(ans)

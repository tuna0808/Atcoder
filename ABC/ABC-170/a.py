L = list(map(int, input().split()))
for l in range(len(L)):
    if L[l]==0:
        ans = l+1
print(ans)    
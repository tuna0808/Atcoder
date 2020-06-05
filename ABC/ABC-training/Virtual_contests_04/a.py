N = int(input()) 
H = list(map(int, input().split()))
sub = []
for i in range(N-1):
    sub.append(H[i+1]-H[i])
#print(sub)
ans = 0
tmp = 0
for s in sub:
    if s <= 0:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
ans = max(ans, tmp)


print(ans)
    




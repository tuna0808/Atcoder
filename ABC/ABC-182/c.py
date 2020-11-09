import itertools

N = input()
ans = 20
for i in itertools.product([0, 1], repeat=len(N)):
    #print(i)
    st = ""
    for k, j in enumerate(i):
        
        if j == 1: st = st + N[k]
    tmp = 0
    for s in st:
        tmp += int(s)
    if tmp % 3==0:
        ans = min(ans, len(N) - len(st))
        #print(ans)
if ans == len(N):
    print(-1)
else:
    print(ans)



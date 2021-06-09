N = int(input()) 
ls = [0] * (N+1) 
ans = 0

for i in range(1,N+1):
    for j in range(i, N+1, i):
        ls[j] += 1

for i,l in enumerate(ls):
    ans += i*l

print(ans)



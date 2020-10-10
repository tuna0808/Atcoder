N = int(input())
ans = 0
cnt = 0
tmp = 0
for i in range(1, N):
    if i**2 >= N:break
    for j in range(i, N):
        if i * j < N:
            ans += 1
        else: break
    tmp += 1

print(ans*2 - tmp)
N = int(input())
L = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if i % 2 == 0:
        if L[i] % 2 == 1: cnt += 1
print(cnt)
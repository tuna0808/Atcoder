X, N = map(int, input().split())
P = sorted(list(map(int, input().split())))
ans = -1
diff = 100000
for i in range(-10,110):
    if i in P: continue
    if diff > abs(i-X):
        diff = abs(i-X)
        ans = i
print(ans)

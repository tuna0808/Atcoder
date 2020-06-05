N = int(input())
P = list(map(int, input().split()))
count = 0
mini = P[0]
for p in P:
    if p <= mini:
        count += 1
    mini = min(mini, p)
print(count)
n = int(input())
S = ["".join(sorted(input())) for _ in range(n)]
counters = {}

for s in S:
    if s in counters:
        counters[s] += 1
    else:
        counters[s] = 1

ans = 0
for v in counters.values():
    if v == 1: continue
    ans += int(v * (v - 1) / 2)
print(ans)
N, W = map(int, input().split())
ls = []
for i in range(N):
    ls.append(list(map(int, input().split())))


table = [0 for i in range(2*(10**5)+5)]
for s, t, p in ls:
    table[s] += p
    table[t] -= p

table_cs = [0]
for t in table:
    table_cs.append(table_cs[-1] + t)

mx = max(table_cs)
if mx > W:
    print("No")
else:
    print("Yes")

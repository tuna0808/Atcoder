import itertools
N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]
ls = []
seq = [i for i in range(N)]
for p in list(itertools.permutations(seq)):
    if p[0]!=0:continue
    tmp = 0
    st = p[0]
    ed = p[-1]
    for i in range(len(p) - 1):
        tmp += T[p[i]][p[i + 1]]
    tmp += T[ed][st]
    ls.append(tmp)
cnt = 0
for l in ls:
    if l == K: cnt += 1
print(cnt)
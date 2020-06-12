import itertools
ls = map(int, input().split())

c = itertools.combinations(ls, 3)
ans_l = []
for v in c:
    ans_l.append(sum(list(v)))
print(sorted(ans_l)[-3])

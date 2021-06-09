A,B = map(int, input().split())

pls_ls = []
minus_ls = []
ans_ls = []

pls = 1
for _ in range(A):
    pls_ls.append(pls)
    pls += 1

minus = -1
for _ in range(B):
    minus_ls.append(minus)
    minus -= 1

sum_pls = sum(pls_ls)
sum_minus = 0 - sum(minus_ls)

diff = sum_pls - sum_minus

if diff > 0:
    tmp = minus_ls.pop(-1)
    minus_ls.append(tmp-diff)
elif diff < 0 :
    tmp = pls_ls.pop(-1)
    pls_ls.append(tmp-diff)
else:
    pass

ans_ls = pls_ls + minus_ls

print(*ans_ls, sep=' ')




N, D, H = map(int, input().split())

ls = []

for n in range(N):
    L = list(map(int, input().split()))
    ls.append(L)

B_ls = []

for L in ls:
    a = (H-L[1])/ (D-L[0])
    b = H - a*D
    B_ls.append(b)

ans = max(B_ls)
if ans < 0 :
    print(0)
else:
    print(ans)
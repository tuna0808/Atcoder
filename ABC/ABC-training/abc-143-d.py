# 二分探索
def binary_search(border, b):
    ok = b
    ng = n
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if L[mid] < border:
            ok = mid
        else:
            ng = mid

    return ok

# O(N^2logN)
n = int(input())
L = sorted(list(map(int, input().split())))
ans = 0

for a in range(0,n-1):
    for b in range(a+1, n):
        a_b = L[a] + L[b]
        ans += binary_search(a_b, b) - b

print(ans)
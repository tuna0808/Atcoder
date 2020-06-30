n, k = map(int, input().split())
A = list(map(int, input().split()))



# 二分探索O(NlogN)
# ここをコメントアウトしないと二分探索コードの中でkを変えてるからバグる.
"""
ans = 0
A_sum = [A[0]]
for i in range(1, n):
    A_sum.append(A_sum[i - 1] + A[i])
    
for i in range(n):
    ng = -1
    ok = n
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if A_sum[mid] >= k: ok = mid
        else: ng = mid
    
    if ok == n: continue
    else: ans += n-ok

    k += A[i]

print(ans)
"""

# しゃくとり法O(N)
ans = 0
r = 0
l = 0
tmp_sum = A[0]
while (True):
    if tmp_sum >= k:
        ans += n - r
        if l == r:
            tmp_sum -= A[l]
            l += 1
            r += 1
            if r == n: break
            tmp_sum += A[r]
            
        else:
            tmp_sum -= A[l]
            l += 1
        
    else:
        r += 1
        if r == n: break
        tmp_sum += A[r]
    

print(ans)
    


    
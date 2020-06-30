N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


#(1)解説PDFっぽい実装(要はしゃくとり) O(N)
sum_a = [0]
sum_b = [0]
ans = 0
for i in range(1,len(A)+1):
    sum_a.append(sum_a[i - 1] + A[i - 1])
for i in range(1,len(B)+1):
    sum_b.append(sum_b[i - 1] + B[i - 1])


j = len(sum_b)-1
for i in range(len(sum_a)):
    if sum_a[i] > K: break
    while (sum_b[j] + sum_a[i] > K):
        j -= 1
    ans = max(ans, i + j)


#print(ans)


#(2)二分探索を使った実装 O(NlogM)

# 下の配列を累積和にしとく
for i in range(1,N):
    A[i] += A[i - 1]
for i in range(1, M):
    B[i] += B[i - 1]

# O(N),O(M)かかるからあんま良くないが複数の実装をする都合でinsert()使用.
A.insert(0, 0)
B.insert(0,0)
ans = 0

#　各A[i]について考える.
for i in range(N+1):
    if K - A[i] < 0:
        break
    # 二分探索
    ok = -1
    ng = M+1
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if B[mid] <= K - A[i]: ok = mid
        else: ng = mid
        
    ans = max(ans, i + ok)

print(ans)

    





# (3)自分のやろうとしてたしゃくとり法
"""
ans = 0
#from collections import deque
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
A = A[::-1]
B = list(map(int, input().split()))

book = A + B
sum_a = sum(A)
sum_b = sum(B)

l = 0
r = len(A)
time = sum_a
ans = 0
#print(book)
while ((r < len(book))|(l <= len(A))):
    if time + book[r] <= K:
        time += book[r]
        ans = max(ans,len(book[l:r])+1)
        r += 1
    elif r == l:
        r += 1
        l += 1
    else:
        time -= book[l]
        l += 1

    #print(l, r)
    #print(ans)
    #print()

book = B[::-1]+A[::-1]

l = 0
r = len(B)
time = sum_b

while ((r < len(book))|(l <= len(B))):
    if time + book[r] <= K:
        time += book[r]
        ans = max(ans,len(book[l:r])+1)
        r += 1
    elif r == l:
        r += 1
        l += 1
    else:
        time -= book[l]
        l += 1
    


print(ans)
    
"""
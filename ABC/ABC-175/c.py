X, K, D = map(int, input().split())
X = abs(X)
tmp_k = X // D

if K - tmp_k < 0:
    ans = abs(X - (D * K))
else:
    tmp = (K- tmp_k) % 2
    if tmp == 0:
        ans = abs(X - (D * tmp_k))
    else:
        ans = abs(X - D * (tmp_k + 1))
        
print(ans)
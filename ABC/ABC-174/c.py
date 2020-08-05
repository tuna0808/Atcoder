K = int(input())
value = 7
ans = -1
for i in range(K):
    if value % K == 0:
        ans = i + 1
        break
    value = (value % K) * 10 + 7
print(ans)
    

    
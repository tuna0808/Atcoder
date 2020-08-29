n = int(input())
cnt_tb = [0]*(n+1)
for i in range(1, n + 1):
    j = 1
    tmp = i*j
    while (tmp < n+1):
        cnt_tb[tmp] += 1
        j += 1
        tmp = i*j
ans = 0
for i in range(1, len(cnt_tb)):
    ans += i * cnt_tb[i]
print(ans)

    
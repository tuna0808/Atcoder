# 考え方はDPっぽい
n = int(input())
h = list(map(int, input().split()))
ans = "Yes"
bf_max = 0
for now in h:
    if bf_max <= now-1:
        bf_max = now - 1
    elif bf_max <= now:
        bf_max = now
    else:
        ans = "No"
        break


print(ans)

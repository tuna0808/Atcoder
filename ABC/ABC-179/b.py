N = int(input())
cnt = 0
tmp_m = 0
for n in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        tmp_m += 1
    else:
        cnt = max(cnt, tmp_m)
        tmp_m = 0
cnt = max(cnt, tmp_m)
if cnt >= 3:
    print("Yes")
else:
    print("No")
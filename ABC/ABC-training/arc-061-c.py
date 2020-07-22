# bit全探索
s = input()
n = len(s) - 1
ans = 0
for i in range(1 << n):
    tmp_l = []
    sep = 0
    for j in range(n):
        if (i >> j) & 1:
            tmp_l.append(int(s[sep:j + 1]))
            sep = j + 1
    tmp_l.append(int(s[sep:]))
    ans += sum(tmp_l)
print(ans)
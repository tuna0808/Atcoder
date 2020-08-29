s = input()
t = input()
ans = len(t)

for i in range(len(s)):
    if i + len(t) -1  >= len(s): break
    diff = 0
    for j in range(len(t)):
        if s[i+j] != t[j]: diff += 1
    ans = min(ans, diff)
print(ans)


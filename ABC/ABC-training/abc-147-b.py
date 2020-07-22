s = input()
if len(s) % 2 == 0:
    l = s[:int(len(s) / 2)]
    r = s[int(len(s) / 2):]
else:
    l = s[:len(s) // 2]
    r = s[(len(s) // 2) + 1:]
r = r[::-1]
ans = 0
for i in range(len(l)):
    if l[i] != r[i]: ans += 1
print(ans)
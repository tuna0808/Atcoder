n = int(input())
s = input()
a = 0
b = 0
for c in s:
    if c == "R": a += 1
ans = max(a,b)
for i in range(n):
    if s[i] == "R": a -= 1
    else: b += 1
    ans = min(ans, max(a, b))
print(ans)








    

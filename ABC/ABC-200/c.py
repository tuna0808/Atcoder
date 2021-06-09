N = int(input()) 
L = list(map(int, input().split()))
L2 = []
ans = 0
for l in L:
    L2.append(l%200)

dic = {}
for l in L2:
    if l in dic:
        dic[l] += 1
    else:
        dic[l] = 1

for l in L2:
    ans += dic[l] - 1
    dic[l] -= 1

print(ans)
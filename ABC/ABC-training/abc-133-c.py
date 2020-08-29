l, r = map(int, input().split())
ans = 2020

for i in range(l, min(r + 1, l + 4040)):
    for j in range(i + 1, min(r + 1, l + 4040)):
        if i * j % 2019 < ans:
            ans = i * j % 2019
print(ans)
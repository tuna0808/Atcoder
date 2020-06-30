n = int(input())

L = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, (n // i)+1):
        L[i * j] += 1

i = 0
ans = 0
for i in range(len(L)):
    ans += i *L[i]

print(ans)

 
        
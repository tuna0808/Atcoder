N = input()
full_len = len(N)
half_len = full_len // 2
flag = full_len % 2
length = half_len + flag

n = int(N[:length])
N = int(N)
ans = 0

for i in range(1, n + 1):
    if int(str(i) + str(i)) <= N: ans += 1


print(ans)








"""
#print(N,n,flag,half_len,full_len)

ans = 0
ls = [9,90,900,9000,90000,900000]
for i in range(half_len - 1):
    ans += ls[i]


for i in range(10 ** (half_len - 1 + flag), n+1):
    #print(i)
    if int(str(i) + str(i)) <= N: ans += 1

print(ans)
"""
    
    
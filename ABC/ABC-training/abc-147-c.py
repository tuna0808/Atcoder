n = int(input())
dic = {i+1: [] for i in range(n)}

for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        dic[i+1].append((x, y))
#print(dic)
ans = 0
for i in range(1 << n):
    flag = 0
    s = str(bin(i))
    cnt = s.count("1")
    #print(s,cnt)

    for j in range(n):
        if (i >> j) & 1:
            for x, y in dic[j + 1]:
                if str(bin((i>>(x-1))))[-1] == str(y):
                    continue
                else:
                    flag = 1
                    break
            
            
            
    if flag != 1:
        ans = max(ans, cnt)

print(ans)


            

N = int(input())
A = list(map(int, input().split()))
dic = {i+1:a for i,a in enumerate(A)}
dic2 = sorted(dic.items(), key=lambda x:x[1])
ls = []
for i in range(len(dic2)):
    ls.append(dic2[i][0])

print(*ls, sep=" ")
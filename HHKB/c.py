N = int(input())
P = list(map(int, input().split()))
output = []
dic = {i: False for i in range(10**6)}
dic[0] = True
pp = 1
mi = 0

for p in P:
    if p == mi:
        mi = pp
        dic[pp] = True
        output.append(mi)
    else:
        dic[p] = True
        output.append(mi)

    if dic[pp]:
        while (dic[pp]):
            pp += 1
    #if mi == pp:
        
    #print(mi, pp)    

print(*output, sep="\n")

        

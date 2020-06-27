n = int(input())
imos_l = [0]*(10**6+2)
for _ in range(n):
    a, b = map(int, input().split())
    imos_l[a] += 1
    imos_l[b + 1] -= 1
    
cu_sum = [0]
for i in range(len(imos_l)):
    cu_sum.append(cu_sum[i] + imos_l[i])
#print(cu_sum[:10])

print(max(cu_sum))
    
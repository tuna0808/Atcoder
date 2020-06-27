import collections
N = int(input()) 
A = sorted(list(map(int, input().split())))
unique_count = collections.Counter(A)
A_count1 = []
A_unique = list(set(A))
baisu = [0]*(10**6+1)

for k,v in unique_count.items():
    if v == 1: A_count1.append(k)

for a_unique in A_unique:
    for i in range(a_unique*2,10**6+1,a_unique):
        baisu[i] = 1

ans = 0

for a_count1 in A_count1:
    if baisu[a_count1]==0: ans += 1

print(ans)


















import collections
N = int(input())
A = list(map(int, input().split()))

dic = collections.Counter(A)
for a in A:
    if (a-1 in dic) & (a+1 in dic): 
        dic[a-1] += 1
        dic[a+1] += 1

    elif (a+1 in dic):
        dic[a+1] += 1
        dic[a-1] = 1
    elif (a-1 in dic):
        dic[a-1] += 1
        dic[a+1] = 1
    else:
        dic[a+1] = 1
        dic[a-1] = 1

print(max(dic.values()))
        



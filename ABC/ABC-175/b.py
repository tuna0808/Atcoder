import itertools
#import math
N = int(input())
L = list(map(int, input().split()))
cnt = 0
tmp_l = list(itertools.combinations(L,3))
for ls in tmp_l:
    if (ls[0] + ls[1] > ls[2]) & (ls[1] + ls[2] > ls[0]) & (ls[0] + ls[2] > ls[1]):
        if (ls[0] != ls[1] ) & (ls[1] != ls[2] ) & (ls[0] != ls[2] ):
            cnt += 1
print(cnt)








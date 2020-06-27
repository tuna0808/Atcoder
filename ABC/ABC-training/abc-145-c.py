import itertools
import math
N = int(input())
x_y = {i : list(map(int, input().split())) for i in range(N)}
P = list(itertools.permutations(range(N)))
tmp = 0
for p in P:
    for n in range(N-1):
        #print(tmp)
        tmp += math.sqrt((x_y[p[n]][0] - x_y[p[n+1]][0])**2 + (x_y[p[n]][1] - x_y[p[n+1]][1])**2)

print(tmp/len(P))


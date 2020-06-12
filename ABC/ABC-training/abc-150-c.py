import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
#print(P,Q)
l = [i for i in range(1,N+1)]
count = 1
count_p = 0
count_q = 0

for v in itertools.permutations(l):
    #print(v)
    if v == P:
        count_p = count
    if v == Q:
        count_q = count

    if (count_p != 0) & (count_q != 0):
        ans = abs(count_p - count_q)
        break
    else:
        count += 1

print(ans)
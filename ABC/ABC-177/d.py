import collections
N, M = map(int, input().split())
dic = {i + 1: set() for i in range(N)}

for m in range(M):
    A, B = map(int, input().split())
    dic[A].add(B)
    dic[B].add(A)


vi_n = [i + 1 for i in range(N)]
vi_d = set()
stack = [i+1 for i in range(N)]
while (len(vi_d) < N):
    v = stack.pop()
    if v in vi_d:
        continue
    vi_d.add(v)

    for node in dic[v]:
        stack.append(node)
        vi_n[node - 1] = vi_n[v - 1]


c = collections.Counter(vi_n)
c_l = list(c.values())
#print(c_l)
print(max(c_l))
    


    



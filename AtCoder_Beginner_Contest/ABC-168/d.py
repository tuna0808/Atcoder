from collections import deque

N, M = map(int, input().split())
neib = {i+1:[] for i in range(N)}
for i in range(M):
  a, b = map(int, input().split())
  neib[a].append(b)
  neib[b].append(a)

mitishil = {i+1:-1 for i in range(1,N)}


q = deque()
q.append(1)
while(q):
  v = q.popleft()
  ls = neib[v]
  
  for l in ls:
    
    if (l == 1): continue
    if (mitishil[l] == -1):
      mitishil[l] = v
      q.append(l)
    
print("Yes")
for i in mitishil.values():
  print(i)




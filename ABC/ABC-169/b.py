
N = int(input()) 
A = list(map(int, input().split()))
S = set(A)
if 0 in S:
  print(0)
  exit()
 
upp = 10**18
ans = 1
#print(A)
for a in A:
  ans *= a
  if ans > upp:
    ans = -1
    break
 
print(ans)
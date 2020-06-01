N = int(input())
A = list(map(int, input().split()))

d = 1
count = 1
i = 0

for a in A:
  if d < a:
    count = -1
    break
  else:
    d = 2**(d-a)
    i += 1
    if i == len(A):
      break
    else:
      count += d

    

print(count)
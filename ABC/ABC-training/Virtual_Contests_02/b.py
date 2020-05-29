import copy
N = int(input())
output = []
dic = {}
A = []

for i in range(N):
  num = int(input())
  A.append(num)
  dic[i] = num

A = sorted(A)
max_1 = A[-1]
max_2 = A[-2]

for i in range(N):
  tmp = dic[i]
  if tmp == max_1:
    output.append(max_2)
  else:
    output.append(max_1)
print(*output, sep="\n")
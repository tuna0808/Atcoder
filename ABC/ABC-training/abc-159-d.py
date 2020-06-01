import collections
N = int(input())
A = list(map(int, input().split()))
C = collections.Counter(A)
comb = 0
output = []

for k,v in C.items():
  comb += int(v*(v-1)/2)

for a in A:
  output.append(comb - (C[a]-1))

print(*output, sep="\n")

# 累積和
N, Q = map(int, input().split())
S = input()
count_ac = [0]
output = []

count = 0
for i in range(N-1):
  if S[i]+S[i+1] == "AC": 
    count += 1
    count_ac.append(count)
  else:
    count_ac.append(count)

for _ in range(Q):
  l, r = map(int, input().split())
  output.append(count_ac[r-1]-count_ac[l-1])

print(*output, sep="\n")

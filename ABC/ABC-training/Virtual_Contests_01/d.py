# 累積和を使用.
N = int(input())
S = input()

sum_w = [0]
sum_e = [0]

count = 0
for i in range(N-1):
  if S[i] == "W":
    count += 1
  sum_w.append(count)

count = 0
for i in range(N-1,0,-1):
  if S[i] == "E": 
    count += 1
  sum_e.append(count)
sum_e = sum_e[::-1]

sumu = [x+y for x, y in zip(sum_w, sum_e)]

print(min(sumu))
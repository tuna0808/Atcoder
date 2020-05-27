W = input()
dic = {}

for w in W:
  if w in dic:
    dic[w] += 1
  else:
    dic[w] = 1

count = 0
for i in dic.values():
  if i % 2 == 0: count += 1

if count == len(dic): print("Yes")
else: print("No")
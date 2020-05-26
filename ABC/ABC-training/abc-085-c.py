N, Y = map(int, input().split())
ans = [-1,-1,-1]
for x in range(N+1):
  for y in range(N+1):
    z = N-x-y
    if z < 0: continue

    if (10000*x + 5000*y + 1000*z) == Y: 
      ans[0]= x
      ans[1]= y
      ans[2]= z
      break
    else: continue

if ans[0]==-1:print("-1 -1 -1")
else:
  #print(f"{ans[0]} {ans[1]} {ans[2]}")
  print("{} {} {}".format(ans[0],ans[1],ans[2]))# ABC-085時点はf文字列に未対応のため.formatを使用.




S = input()
ans = []
for s in S:
  if s=="B":
    if len(ans)==0: continue
    else: ans.pop()
  else:
    ans.append(int(s))

ans = map(str, ans)
print("".join(ans))

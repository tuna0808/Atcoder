N = int(input())

def dfs(s):
  if int(s) > N:
    return 0
  count = 1 if all(s.count(x) > 0 for x in ["7","5","3"]) else 0 

  for i in ["7","5","3"]:
    count += dfs(s+i)

  return count


print(dfs("0"))


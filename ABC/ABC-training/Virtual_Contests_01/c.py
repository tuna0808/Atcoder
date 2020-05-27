H, W = map(int, input().split())
grid = []
flag = 1
for h in range(H):
  S = input()
  tmp = []
  for s in S:
    tmp.append(s)
  grid.append(tmp)

for h in range(H):
  for w in range(W):
    mark = grid[h][w]
    if mark == ".": continue

    if h-1 >= 0:
      up = grid[h-1][w]
    else: up = "."

    if h+1 <= H-1:
      down = grid[h+1][w]
    else: down = "."

    if w-1 >= 0:
      left = grid[h][w-1]
    else: left = "."
    
    if w+1 <= W-1:
      right = grid[h][w+1]
    else: right = "."

    if (up != "#") & (down != "#") & (right != "#") & (left != "#"): 
      flag = 0
      break

if flag == 1: print("Yes")
else:print("No")

    


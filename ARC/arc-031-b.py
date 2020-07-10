land = ["xxxxxxxxxxxx"]
for _ in range(10):
    land.append("x" + input() + "x")
land.append("xxxxxxxxxxxx")
print(land)

land_num = [[0]*12 for _ in range(12)]

num = 1
for i in range(1, 11):
    for j in range(1, 11):
        if land[i][j] == "": continue
        stack = [(i, j)]
        while (stack):
            (x, y) = stack.pop()

        num += 1
            

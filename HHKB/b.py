H, W = map(int, input().split())
ls = []
suma = 0
for i in range(H):
    S = input()
    cnt = 0
    for s in S:
        if cnt == 0:
            if s == ".":
                cnt += 1
                continue
            else:
                continue
        elif cnt == 1:
            if s == ".":
                suma += 1
                continue
            else:
                cnt = 0
                continue
        
    ls.append(S)

for i in range(W):
    cnt = 0
    for j in range(H):
        
        if cnt == 0:
            if ls[j][i] == ".":
                cnt += 1
                continue
            else:
                continue
        elif cnt == 1:
            if ls[j][i] == ".":
                suma += 1
                
                continue
            else:
                cnt = 0
                continue
print(suma)

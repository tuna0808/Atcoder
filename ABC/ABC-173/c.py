h, w, k = map(int, input().split())
C = [input() for i in range(h)]
ans = 0

for rows in range(1 << h):
    for cols in range(1 << w):
        cnt = 0
        for i in range(h):
            if (rows >> i) & 1: continue
            for j in range(w):
                if (cols >> j) & 1:
                    continue
                else:
                    if C[i][j] == "#": cnt += 1
        if cnt == k: ans += 1

print(ans)
                
                

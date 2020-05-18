n, m = map(int, input().split())
dicts = {key: [False,0] for key in range(1, n+1)}

for i in range(m):
    p, s = input().split()
    p = int(p)
    if s == "AC":
        dicts[p][0] = True
        continue
    else:
        if dicts[p][0]==True:
            continue
        else:
            dicts[p][1] += 1
        
ans_list = [v[1] for k, v in dicts.items() if v[0]==True]
ans_n = len(ans_list)
penal = sum(ans_list)
print(ans_n, penal)
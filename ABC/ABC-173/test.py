import itertools
import numpy as np
h, w, k = map(int, input().split())
C_list = [input() for i in range(h)]
C_num = []
for c_r in C_list:
    r_l = []
    for v in c_r:
        if v == "#": r_l.append(1)
        else: r_l.append(0)
    C_num.append(r_l)
C_num = np.array(C_num)





comb = []
for i in range(h+1):  # 何行選ぶか
    for j in range(w+1):  #何列選ぶか
        r = itertools.combinations(range(h), i)# 行をi個選ぶ組み合わせ
        c = itertools.combinations(range(w), j)  # 列をj個選ぶ組み合わせ
        comb.append([r, c])



ans = 0
for R, C in comb:
    for r in R:
        for c in C:
            #print(f"行:{list(r)}")
            #print(f"列:{list(c)}")
            tmp_l = C_num.copy()
            count = 0
            for r_value in r:
                tmp_l[r_value, :] = tmp_l[r_value, :] - 1
            for c_value in c:
                tmp_l[:,c_value] = tmp_l[:,c_value] - 1
            for AAA in tmp_l.flatten():
                if AAA == 1: count += 1
            

            
            if count == k: ans += 1

print(ans)


        
        
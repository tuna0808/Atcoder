# 方針は間違っていないはず, なんかデカめのコーナーケースを見落としてる気がする
# 提出結果のpython, AC, D問題を確認して理解する(解説動画→ 動画のC++の実装を読む)→ sublimeのインストール


import math
A, B, K  = map(int, input().split())
S = ""
A -= 1
cnt = 0


while(A+B > 0):
    tmp = math.factorial(A+B) / (math.factorial(A)*math.factorial(B))
    #print(tmp + cnt, A,B)
    if tmp+cnt > K:
    #if tmp > K:
        S += "a"
        A -= 1

    elif tmp+cnt < K: 
    #elif tmp < K:
        S += "b"
        B -= 1
        cnt += tmp

    else:
        #print("else")
        A += 1
        #print(A,B)
        if B == 0: S += "b"
        
        for b in range(B):
            S += "b"
        for b in range(A):
            S += "a"
        break



print(S)
#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa




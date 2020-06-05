D = sorted(list(map(int, input().split())))
S = sorted(list(map(int, input().split())))
D_v = D[0]*D[1]*D[2]
S_v = S[0]*S[1]*S[2]

while(len(D)>0):
    d = D.pop()
    s = S.pop()
    if d < s:
        print(0)
        exit()

print(D_v // S_v)


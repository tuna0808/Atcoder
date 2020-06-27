N = int(input())
L = list('abcdefghijklmnopqrstuvwxyz')
if N <= 26:
    print(L[N - 1])
    exit()

L = list('zabcdefghijklmnopqrstuvwxy')
ans_l = []


while (True):
    syou = N // 26
    amari = N % 26
    ans_l.append(L[amari])

    if amari == 0:
        N = syou - 1
    else:
        N = syou
    
    if N <= 26: break
    
if N == 26: N = 0
ans_l.append(L[N])

ans_l = ans_l[::-1]
print(*ans_l, sep="")
    

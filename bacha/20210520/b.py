import itertools

N = int(input())
LS = []
ans = 0
for n in range(N):
    LS.append(list(map(int, input().split())))

l = 0
r = 10**9 + 4


while(r-l > 1):
    mid = (l+r) // 2
    #print(mid)
    unique = set()

    for ls in LS:
        k = ""
        for i in ls:
            if i >= mid: k += "1"
            else: k += "0"
        
        unique.add(int(k,2))
    
    if len(unique) >= 3:
        for V in itertools.permutations(unique, 3):
            tmp = V[0]| V[1] | V[2]

            if tmp & 31 == 31:
                l = mid
                ans = mid
            else:
                r = mid
    elif len(unique) == 2:
        for V in itertools.permutations(unique, 2):
            
            tmp = V[0]| V[1]

            if tmp & 31 == 31:
                l = mid
                ans = mid
            else:
                r = mid

    elif len(unique) == 1:
        for V in itertools.permutations(unique, 1):
            tmp = V[0]
            if tmp & 31 == 31:
                l = mid
                ans = mid
            else:
                r = mid




print(ans)

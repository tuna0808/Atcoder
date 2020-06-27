N = int(input())
mi = 10**15
ans_i = 0
ans_j = 0
for i in range(2, 10**6+1):
    if N % i == 0:
        j = N // i
        if mi > (i+j-2):
            mi = i+j-2
            ans_i = i
            ans_j = j
if ans_i+ans_j != 0:print(ans_i+ans_j-2)
else:print(N-1)
        



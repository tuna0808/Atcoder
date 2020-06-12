#import sys
#sys.path.append('../../')
#from librarys import prime_factorization

def factorization(n):# 計算量O(√N)
    arr = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp]=1

    if arr==[]:
        arr[n] = 1

    return arr



x = int(input())
while(True):
    p = factorization(x)
    if (len(p)==1) & (x in p):
        break
    else:
        x += 1

print(x)


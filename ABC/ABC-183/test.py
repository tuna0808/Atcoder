# (1) [数値単独型] 
# 入力->3
# 出力->3
N = int(input()) 

# (2) [数値リスト変換型] 
# 入力->3 4 
# 出力->[3, 4]
L = list(map(int, input().split()))

# (3) [数値複数変数型] 
# 入力->3 4 
# 出力-> N=3, M=4
N, M = map(int, input().split())



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
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

start_100 = A + (100 - A%100)
if start_100 <= B: count_100 = 1
else: count_100 = 0

if B-start_100 < 0: pass
else: 
    count_100 += (B-start_100) // 100


#print(count_100)
start_400 = A + (400 - A%400)
if start_400 <= B: count_400 = 1
else: count_400 = 0

if B-start_400 < 0: pass
else: 
    count_400 += (B-start_400) // 400
#print(count_400)

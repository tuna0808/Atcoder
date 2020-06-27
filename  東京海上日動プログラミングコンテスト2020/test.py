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
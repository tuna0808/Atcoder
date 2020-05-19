N = int(input())
h = list(map(int, input().split()))

dp_table = [float("inf")]*N # 0~N-1まで
dp_table[0] = 0

for i in range(N-1): # 0~N-1までだが+1して扱う(1~N)
    dp_table[i+1] = min(dp_table[i]+abs(h[i]-h[i+1]), dp_table[i+1])
    if i-1>=0:
        dp_table[i+1] = min(dp_table[i-1]+abs(h[i-1]-h[i+1]), dp_table[i+1])
        
print(dp_table[N-1])
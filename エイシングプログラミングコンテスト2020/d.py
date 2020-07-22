def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

N = int(input())
x = list(input())
count = 0
for i in x:
    if i == "1": count += 1
    
output = []
for n in range(N):
    cnt = 1
    tmp_count = count
    y = x.copy()
    if y[n] == "1":
        y[n] = "0"
        tmp_count -= 1
    else:
        y[n] = "1"
        tmp_count += 1

    s = "".join(y)
    v = int(s, 2) % tmp_count
    tmp_count = popcount(v)

    while (v > 0):
        v %= tmp_count
        tmp_count = popcount(v)
        cnt += 1

    output.append(cnt)

print(*output, sep="\n")

    
        
    




N = int(input())
A = list(map(int, input().split()))

ans = 0 #初期位置が0なので, 最低でも0にはなる
b = 0  # 各フェーズでのAの累積和を保持
s = 0  # 各フェーズ終了時点での位置を保持
max_b = 0  # 各フェーズでのAの累積和の最大値を保持

# 最初何も累積和を取らない初期地点はフェーズ-1とする # 
for i in range(N):# フェーズiスタート
    b += A[i] # フェーズiの段階の累積和
    max_b = max(b, max_b) # そこまでの最大
    ans = max(ans, s + max_b) #今までの最大(ans)と, 現在位置(フェーズi-1終了位置) + フェーズi時点での累積和の最大(max_b)を足したのどっちがでかいか比較
    s += b # 終了位置を更新
print(ans)





"""
# Aの累積和
A_cs = [0]
for a in A:
    A_cs.append(A_cs[-1] + a)

# 各段階での終了地点を算出
end_p = [0]
for a_cs in A_cs[1:]:
    end_p.append(end_p[-1] + a_cs)



# 累積和における, 各段階のmax値を保持
A_cs_max = [0]
for a_cs in A_cs[1:]:
    if A_cs_max[-1] < a_cs:
        A_cs_max.append(a_cs)
    else:
        A_cs_max.append(A_cs_max[-1])
#print(A_cs)
#print(end_p)
#print(A_cs_max)

ans = 0
for i in range(len(end_p)):
    ans = max(ans, end_p[i] + A_cs_max[i])
print(ans)
"""
N = int(input()) 
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

B_A_dic = {}
B_C_dic = {}

for i in range(N):
    #B_A_dic
    if B[C[i]-1] in B_A_dic:
        B_C_dic[B[C[i]-1]] += 1
    else:
        B_A_dic[B[C[i]-1]] = 0
        B_C_dic[B[C[i]-1]] = 1

for a in A:
    if a in B_A_dic:
        B_A_dic[a] += 1
ans = 0
for a,b in zip(B_A_dic.values(), B_C_dic.values()):
    ans += a*b

print(ans)


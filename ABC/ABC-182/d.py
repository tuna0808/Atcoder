N = int(input())
A = list(map(int, input().split()))
tmp_1 = [0]
now = 0


A_cs = [A[0]]
for i in range(1, len(A)):
    A_cs.append(A_cs[-1] + A[i])

for i in A_cs:
    now += i
    tmp_1.append(now)


ans = max(tmp_1)
tmp_2 = max(tmp_1)
ind = [i for i, v in enumerate(tmp_1) if v == max(tmp_1)][-1]


for a in A[:ind]:
    tmp_2 += a
    ans = max(ans, tmp_2)

tmp_2 = max(tmp_1)
for a in A[:ind][::-1]:
    a *= -1
    tmp_2 += a
    ans = max(ans, tmp_2)


print(ans)




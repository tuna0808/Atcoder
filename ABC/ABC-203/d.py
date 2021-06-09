N, K = map(int, input().split())
A = []

for n in range(N):
    A_col = list(map(int, input().split()))
    A.append(A_col)

print(A)
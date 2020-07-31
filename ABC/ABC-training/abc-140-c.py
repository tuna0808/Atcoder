n = int(input())
B = list(map(int, input().split()))
A = [0] * n
A[0] = B[0]
for i in range(1, n - 1):
    A[i] = min(B[i - 1], B[i])
A[n - 1] = B[-1]

print(sum(A))

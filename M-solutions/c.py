n, k = map(int, input().split())
A = list(map(int, input().split()))

output = []
count = 0
for i in range(k, n):
    if A[i] > A[count]:
        output.append("Yes")
    else:
        output.append("No")
    count += 1
    
print(*output, sep="\n")
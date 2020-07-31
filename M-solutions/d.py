n = int(input())
given_A = list(map(int, input().split()))
A = []
for kabuka in given_A:
    if len(A) > 0 and kabuka == A[-1]:
        continue
    else:
        A.append(kabuka)

# 株価が全て同じ時のコーナーケース
if len(A) == 1:
    print(1000)
    exit()

money = 1000
stock = 0
n = len(A)
for i in range(len(A)):
    if i == 0:
        if A[i] < A[i + 1]:
            stock = money // A[i]
            money = money % A[i]
    elif i == n - 1:        
        if A[i - 1] < A[i]:
            money += stock*A[i]
            stock = 0
    else:
        if (A[i - 1] < A[i]) & (A[i] > A[i + 1]):
            money += stock*A[i]
            stock = 0
        elif (A[i - 1] > A[i]) & (A[i] < A[i + 1]):
            stock = money // A[i]
            money = money % A[i]
print(money)
            



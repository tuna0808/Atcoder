import collections 
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
dic = collections.Counter(A)
suma = sum(A)
output = []

for q in range(Q):
    b, c = map(int, input().split())
    if b in dic:
        suma += dic[b] * c
        suma -= dic[b] * b
        dic[c] += dic[b]
        dic[b] = 0

    output.append(suma)

print(*output, sep="\n")


    

    

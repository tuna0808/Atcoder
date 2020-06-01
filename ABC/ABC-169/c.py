import math

A, B = input().split()
A = int(A)
sei = int(B[0])
syou = int(B[2]+B[3])
#print(sei,syou)
B = sei*100 + syou
###print(B)
#print(A*B)
ans = (A*B) // 100 




print(ans)


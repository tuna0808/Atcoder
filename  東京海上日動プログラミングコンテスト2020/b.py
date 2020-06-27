A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input()) 
flag = 0

if A < B:
    a = V*T + A
    b = W*T + B
    if a >= b:
        flag = 1


else:
    a = A - V*T
    b = B - W*T
    if a <= b:
        flag = 1

if flag==1:
    print("YES")
else:
    print("NO")
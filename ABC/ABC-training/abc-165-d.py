A, B, N = map(int, input().split())
x = min(N,B-1)

ans = int(A/B*x)-A*int(x/B)
print(ans)
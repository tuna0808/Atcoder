n, k, m = map(int, input().split())
a = list(map(int, input().split()))

border = n * m
if n * m - sum(a) > k:
    print('-1')
else:
    print(max(0,n * m - sum(a)))



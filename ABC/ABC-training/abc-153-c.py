N, K = map(int, input().split())
H = sorted(list(map(int, input().split())), reverse=True)

H = H[K:]

print(sum(H))

